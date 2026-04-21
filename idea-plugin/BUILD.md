# IDEA 插件构建和安装指南

## 构建插件

由于 Gradle Wrapper 文件缺失，推荐使用 IntelliJ IDEA 的内置 Gradle 支持来构建插件。

### 方法一：使用 IDEA 构建（推荐）

1. 使用 IntelliJ IDEA 打开 `idea-plugin` 目录
2. IDEA 会自动识别为 Gradle 项目并下载依赖
3. 打开 Gradle 工具窗口（View → Tool Windows → Gradle）
4. 展开 `idea-plugin → Tasks → intellij`
5. 双击 `buildPlugin` 任务
6. 构建完成后，插件 ZIP 文件位于：`idea-plugin/build/distributions/`

### 方法二：安装 Gradle 后构建

如果需要命令行构建：

1. 安装 Gradle 8.5+：https://gradle.org/install/
2. 在 `idea-plugin` 目录下运行：
   ```bash
   gradle wrapper
   ./gradlew buildPlugin
   ```

## 安装插件

1. 打开 IDEA 设置：`File → Settings`（Windows/Linux）或 `IntelliJ IDEA → Preferences`（Mac）
2. 导航到：`Plugins`
3. 点击齿轮图标 ⚙️ → `Install Plugin from Disk...`
4. 选择构建生成的 ZIP 文件：`idea-plugin/build/distributions/Git-AI-Commit-1.0.13.zip`
5. 重启 IDEA

## 配置插件

1. 打开设置：`File → Settings → Tools → Git AI Commit`
2. 配置必要字段：
   - Provider：选择 `openai` 或 `anthropic`
   - API Key：输入你的 API 密钥
   - Release Version：当前版本号（如 `1.0.0`）
   - Ticket ID Regex：单号正则表达式（如 `[A-Z]+-\\d+`）

## 使用插件

1. 在项目中进行代码修改
2. 使用 `git add` 暂存改动
3. 在 VCS 菜单中选择：`VCS → Git AI Commit → Generate AI Commit Message`
4. 插件会生成符合规范的提交消息

## 提交消息格式

生成的提交消息格式为：`【类型】（版本号[-单号]）中文摘要`

支持的类型：
- `feature`、`bugfix`、`docs`、`style`、`build`：必须包含单号
- `refactor`、`revert`、`config`：只包含版本号

示例：
- `【feature】（1.0.0-PROJ-123）添加用户登录功能`
- `【refactor】（1.0.0）重构数据库连接层`
