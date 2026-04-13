"""Change classifier module.

Classifies git diff changes into categories (database, api, business_logic,
config, ui) using file path patterns, file extensions, and code content
keywords. Extracts key change information (functions, classes) for each file.
"""

import ast
import os
import re

CATEGORY_PRIORITY = {
    "database": 5,
    "api": 4,
    "business_logic": 3,
    "config": 2,
    "ui": 1,
}

PRIORITY_ORDER = ["database", "api", "business_logic", "config", "ui"]

CATEGORY_PATH_PATTERNS = {
    "database": [
        "migrations/", "migrate/", "alembic/",
        "seeds/", "seeders/", "fixtures/",
        "entity/", "entities/", "repository/",
        "mapper/", "dao/",
        "models/", "model/",
        "Models/", "Data/",
    ],
    "api": [
        "controller/", "controllers/",
        "views/", "viewsets/", "serializers/",
        "urls/", "routes/", "api/", "endpoints/",
        "handler/", "handlers/", "router/",
        "Controllers/",
    ],
    "business_logic": [
        "service/", "services/",
        "tasks/", "commands/", "helpers/",
        "usecase/", "usecases/",
        "Services/",
    ],
    "config": [
        "config/", "configs/", "settings/",
        "env/", "properties/",
    ],
    "ui": [
        "components/", "pages/",
        "templates/", "static/", "assets/",
        "styles/", "css/", "scss/",
        "store/", "stores/",
    ],
}

CATEGORY_EXTENSIONS = {
    "database": [".sql", ".prisma"],
    "config": [
        ".yaml", ".yml", ".toml", ".ini", ".cfg", ".conf",
        ".env", ".properties",
    ],
    "ui": [
        ".html", ".htm", ".css", ".scss", ".less", ".sass",
        ".vue", ".jsx", ".tsx", ".svg",
    ],
}

CATEGORY_CONTENT_KEYWORDS = {
    "database": [
        "CREATE TABLE", "ALTER TABLE", "DROP TABLE",
        "CREATE INDEX", "migration", "db.Column",
        "ForeignKey", "relationship", "db.Model",
        "Schema", "@Entity", "@Table", "@Column",
        "models.Model", "models.Field",
    ],
    "api": [
        "@app.route", "@router.", "@api_view",
        "@GetMapping", "@PostMapping", "@RequestMapping",
        "@RestController", "app.get(", "app.post(",
        "router.get(", "router.post(",
        "func (h *Handler)", "gin.Context",
    ],
    "config": [
        "DATABASE_URL", "SECRET_KEY", "API_KEY",
        "os.environ", "process.env", "dotenv",
    ],
    "ui": [
        "render(", "component", "useState",
        "template", "v-model", "v-for",
        "@Component", "ngOnInit",
    ],
}

# Regex patterns for extracting function/class definitions from non-Python files
FUNCTION_PATTERNS = [
    re.compile(r'(?:public|private|protected)?\s+[\w<>\[\]]+\s+(\w+)\s*\('),
    re.compile(r'function\s+(\w+)\s*\('),
    re.compile(r'(?:const|let|var)\s+(\w+)\s*=.*=>'),
    re.compile(r'func\s+(?:\(\w+\s+\*?\w+\)\s+)?(\w+)\s*\('),
]

CLASS_PATTERNS = [
    re.compile(r'class\s+(\w+)'),
    re.compile(r'type\s+(\w+)\s+struct'),
]


def _extract_definitions_regex(lines):
    """Extract function and class names using regex patterns."""
    functions = []
    classes = []
    for line in lines:
        for pattern in FUNCTION_PATTERNS:
            match = pattern.search(line)
            if match:
                name = match.group(1)
                if name not in functions:
                    functions.append(name)
                break
        for pattern in CLASS_PATTERNS:
            match = pattern.search(line)
            if match:
                name = match.group(1)
                if name not in classes:
                    classes.append(name)
                break
    return {"functions": functions, "classes": classes}


def _extract_python_definitions(lines):
    """Extract function and class names from Python code lines using AST.

    Falls back to regex if AST parsing fails.
    """
    source = "\n".join(lines)
    try:
        tree = ast.parse(source)
        functions = [
            node.name for node in ast.walk(tree)
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        ]
        classes = [
            node.name for node in ast.walk(tree)
            if isinstance(node, ast.ClassDef)
        ]
        return {"functions": functions, "classes": classes}
    except SyntaxError:
        return _extract_definitions_regex(lines)


def _build_key_changes(file_info):
    """Build the key_changes list for a file."""
    key_changes = []
    path = file_info["path"]
    change_type = file_info["change_type"]

    if change_type == "added":
        key_changes.append("add file: " + os.path.basename(path))
    elif change_type == "deleted":
        key_changes.append("delete file: " + os.path.basename(path))
    elif change_type == "renamed":
        key_changes.append("rename file: " + os.path.basename(path))

    is_python = path.endswith(".py")
    if is_python:
        added_defs = _extract_python_definitions(file_info.get("added_lines", []))
        deleted_defs = _extract_python_definitions(file_info.get("deleted_lines", []))
    else:
        added_defs = _extract_definitions_regex(file_info.get("added_lines", []))
        deleted_defs = _extract_definitions_regex(file_info.get("deleted_lines", []))

    added_funcs = set(added_defs["functions"])
    deleted_funcs = set(deleted_defs["functions"])
    modified_funcs = added_funcs & deleted_funcs
    new_funcs = added_funcs - modified_funcs
    removed_funcs = deleted_funcs - modified_funcs

    for name in sorted(new_funcs):
        key_changes.append("add function: " + name)
    for name in sorted(modified_funcs):
        key_changes.append("modify function: " + name)
    for name in sorted(removed_funcs):
        key_changes.append("delete function: " + name)

    added_cls = set(added_defs["classes"])
    deleted_cls = set(deleted_defs["classes"])
    modified_cls = added_cls & deleted_cls
    new_cls = added_cls - modified_cls
    removed_cls = deleted_cls - modified_cls

    for name in sorted(new_cls):
        key_changes.append("add class: " + name)
    for name in sorted(modified_cls):
        key_changes.append("modify class: " + name)
    for name in sorted(removed_cls):
        key_changes.append("delete class: " + name)

    return key_changes


def _classify_by_path(path):
    """Classify file by path patterns."""
    for category in PRIORITY_ORDER:
        for pattern in CATEGORY_PATH_PATTERNS.get(category, []):
            if pattern in path:
                return category
    return None


def _classify_by_extension(path):
    """Classify file by extension."""
    _, ext = os.path.splitext(path)
    if not ext:
        return None
    ext = ext.lower()
    for category in PRIORITY_ORDER:
        if ext in CATEGORY_EXTENSIONS.get(category, []):
            return category
    return None


def _classify_by_content(added_lines):
    """Classify file by code content keywords in added lines."""
    if not added_lines:
        return None
    content = "\n".join(added_lines)
    best_category = None
    best_priority = -1
    for category, keywords in CATEGORY_CONTENT_KEYWORDS.items():
        for keyword in keywords:
            if keyword in content:
                priority = CATEGORY_PRIORITY.get(category, 0)
                if priority > best_priority:
                    best_priority = priority
                    best_category = category
                break
    return best_category


def _classify_file(file_info):
    """Classify a single file using three dimensions (path, extension, content).

    Returns tuple of (category, category_source).
    """
    path = file_info["path"]
    candidates = []

    path_cat = _classify_by_path(path)
    if path_cat:
        candidates.append((path_cat, "path"))

    ext_cat = _classify_by_extension(path)
    if ext_cat:
        candidates.append((ext_cat, "extension"))

    content_cat = _classify_by_content(file_info.get("added_lines", []))
    if content_cat:
        candidates.append((content_cat, "content"))

    if not candidates:
        return ("unclassified", "unclassified")

    best = max(candidates, key=lambda x: CATEGORY_PRIORITY.get(x[0], 0))
    return best


def _empty_result(parsed_diff=None):
    """Return empty classification result."""
    default_summary = {
        "total_files": 0, "added": 0, "modified": 0,
        "deleted": 0, "renamed": 0,
        "total_additions": 0, "total_deletions": 0,
    }
    summary = parsed_diff.get("summary", default_summary) if parsed_diff else default_summary
    return {
        "summary": summary,
        "categories": {
            "database": [], "api": [], "business_logic": [],
            "config": [], "ui": [], "unclassified": [],
        },
        "priority_order": PRIORITY_ORDER,
    }


def classify_changes(parsed_diff):
    """Classify parsed diff results into categories.

    Takes the output of parse_diff() and classifies each file into
    database, api, business_logic, config, ui, or unclassified categories.

    Args:
        parsed_diff: Dict with 'summary' and 'files' keys from parse_diff().

    Returns:
        Dict with 'summary', 'categories', and 'priority_order' keys.
    """
    if not parsed_diff or not parsed_diff.get("files"):
        return _empty_result(parsed_diff)

    categories = {
        "database": [], "api": [], "business_logic": [],
        "config": [], "ui": [], "unclassified": [],
    }

    for file_info in parsed_diff["files"]:
        category, category_source = _classify_file(file_info)
        key_changes = _build_key_changes(file_info)
        categories[category].append({
            "path": file_info["path"],
            "change_type": file_info["change_type"],
            "additions": file_info["additions"],
            "deletions": file_info["deletions"],
            "key_changes": key_changes,
            "category": category,
            "category_source": category_source,
        })

    return {
        "summary": parsed_diff["summary"],
        "categories": categories,
        "priority_order": PRIORITY_ORDER,
    }
