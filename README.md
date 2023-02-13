<p align="center">
  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>
</p>

<div align="center">
  
# Nonebot_Plugin_ArkTools
  
_✨ 基于 OneBot 适配器的 [NoneBot2](https://v2.nonebot.dev/) 明日方舟小工具箱插件 ✨_
  
</div>

[![OSCS Status](https://www.oscs1024.com/platform/badge/NumberSir/nonebot_plugin_arktools.svg?size=small)](https://www.oscs1024.com/project/NumberSir/nonebot_plugin_arktools?ref=badge_small)

本人python小萌新，插件有不完善和可以改进之处欢迎各位多提pr和issue

- [功能](#功能)
- [安装](#安装)
- [使用](#如何使用)
- [示例](#图片示例)
- [感谢](#感谢)
- [更新日志](#更新日志)

# 功能
## 已实现：
1. [x] 可以查询推荐的公招标签(截图识别/手动输文字)
2. [x] 可以查询干员的技能升级材料、专精材料、精英化材料、模组升级材料
3. [x] 可以通过网易云点歌，以卡片形式发送
4. [x] 猜干员小游戏，玩法与 [wordle](https://github.com/noneplugin/nonebot-plugin-wordle) 相同
5. [x] 可以查看生日为今天的干员
6. [x] 可以记录当前理智，等回复满后提醒

## 编写中...
1. [ ] 可以查询某种资源在哪个关卡期望理智最低
2. [ ] 根据当前有的资源和需要的资源种类、数量测算最优推图计划
3. [ ] 查询某干员的基础数据：
   1. [ ] 给定等级、信赖、潜能下的基础面板
   2. [ ] 天赋、特性、技能
   3. [ ] 干员种族、势力、身高等基本个人信息
4. [ ] 定时提醒剿灭 / 蚀刻章 / 合约等活动过期

# 安装
- 使用 nb-cli
```
nb plugin install nonebot_plugin_arktools
```
- 使用 pip
```
pip install -U nonebot_plugin_arktools
```

# 如何使用
## 启动注意
 - 每次启动并连接到客户端后会从 __[明日方舟常用素材库](https://github.com/yuanyan3060/Arknights-Bot-Resource)__(__[yuanyan3060](https://github.com/yuanyan3060)__), __[《明日方舟》游戏数据库](https://github.com/Kengxxiao/ArknightsGameData)__(__[Kengxxiao](https://github.com/Kengxxiao)__), __[Arknight-Images](https://github.com/Aceship/Arknight-Images)__(__[Aceship](https://github.com/Aceship)__) 下载使用插件必需的文本及图片资源到本地，已经下载过的文件不会重复下载。下载根据网络情况不同可能耗时 5 分钟左右
 - 如需手动更新，请用命令 __“更新方舟素材”__ 进行更新
 - 如果自动下载失败，请手动下载发行版中的 __“`data.zip`”__ 压缩文件，解压到 __“`nonebot_plugin_arktools/data`”__ 文件夹下，正确放置的文件夹结构应为：
```txt
nonebot_plugin_arktools
├── data
│   ├── arknights
│   │   ├── gamedata
│   │   │   └── excel
│   │   │       └── ...
│   │   ├── gameimage
│   │   │   └── ...
│   │   └── ...
│   ├── fonts
│   │   ├── Arknights-en.ttf
│   │   └── Arknights-zh.otf
│   ├── guess_character
│   │   ├── correct.png
│   │   ├── down.png
│   │   ├── up.png
│   │   ├── vague.png
│   │   └── wrong.png
│   └── ...
├── src
├── test
├── ...
...
```

## .env.env 配置项【必填】

```ini
# 具体见 https://console.bce.baidu.com/ai/?fromai=1#/ai/ocr/app/list
arknights_baidu_app_id="xxx"    # 百度 OCR APP ID
arknights_baidu_api_key="xxx"   # 百度 OCR API KEY

github_raw="xxx"   # 默认为 https://raw.githubusercontent.com，如有镜像源可以替换
github_site="xxx"  # 默认为 https://github.com，如有镜像源可以替换
...
```
各配置项的含义如上。

## 指令
<details>
<summary>详细指令</summary>

### 详细指令
使用以下指令触发，需加上指令前缀
```text
格式：
指令 => 含义
[] 代表参数
xxx/yyy 代表 xxx 或 yyy
```
杂项
```text
方舟帮助 / arkhelp   => 查看指令列表
更新方舟素材          => 手动更新游戏数据(json)与图片
更新方舟数据库        => 手动更新数据库
```
猜干员
```text
猜干员    => 开始新游戏
#[干员名] => 猜干员，如：#艾雅法拉
提示      => 查看答案干员的信息
结束      => 结束当前局游戏
```
今日干员
```text
今日干员 => 查看今天过生日的干员
```
塞壬点歌
```text
塞壬点歌 [关键字] => 网易云点歌，以卡片形式发到群内
```
干员信息
```text
干员 [干员名] => 查看干员的精英化、技能升级、技能专精、模组解锁需要的材料
```
公开招募
```text
公招 [公招界面截图]          => 查看标签组合及可能出现的干员
回复截图：公招               => 同上
公招 [标签1] [标签2] ...    => 同上
```
理智提醒
```text
理智提醒                    => 默认记当前理智为0，回满到135时提醒"
理智提醒 [当前理智] [回满理智] => 同上，不过手动指定当前理智与回满理智"
理智查看                    => 查看距离理智回满还有多久，以及当期理智为多少"
```
</details>

# 图片示例
<details>
<summary>图片们</summary>

## 图片们
<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/218328291-2324ea20-74c4-4182-81ed-4b74950c3ef9.png" width="500" />
</div>

<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/218328307-f71e08ff-2370-4fb9-8898-c76f7e06a168.png" width="500" />
</div>

<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/218328316-9259d9e6-6c2f-40e9-87bd-cee68da240e2.png" width="500" />
</div>

<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/218328320-9ee76c53-dcf2-4245-b302-ea1df7927772.png" width="500" />
</div>

<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/218328326-0fc07fc7-0aa9-42b9-83e1-6eb490f4cff2.png" width="500" />
</div>

<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/218328333-770d08e6-76c6-4087-9d62-75e302ca5f66.png" width="500" />
</div>

<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/218328340-ce4ade0d-d00d-4520-8632-544940a1cc96.png" width="500" />
</div>

<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/218328344-2b9b0cda-3894-451b-9ea0-d7aeec7d200c.png" width="500" />
</div>

<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/218328356-a8a511c4-fa62-481b-af92-71052a087670.png" width="500" />
</div>

<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/218328361-95ae9117-cd5e-4295-982c-9498e0b880fb.png" width="500" />
</div>
</details>


# 感谢
 - __[yuanyan3060](https://github.com/yuanyan3060)__ 的 __[明日方舟常用素材库](https://github.com/yuanyan3060/Arknights-Bot-Resource)__
 - __[Kengxxiao](https://github.com/Kengxxiao)__ 的 __[《明日方舟》游戏数据库](https://github.com/Kengxxiao/ArknightsGameData)__
 - __[Aceship](https://github.com/Aceship)__ 的 __[Arknight-Images](https://github.com/Aceship/Arknight-Images)__
 - __[AmiyaBot](https://github.com/AmiyaBot)__ 的 __[Amiya-bot](https://github.com/AmiyaBot/Amiya-Bot)__
 - __[Strelizia02](https://github.com/Strelizia02)__ 的 __[AngelinaBot](https://github.com/Strelizia02/AngelinaBot)__


# 更新日志
> 2023-02-13 v1.0.4
> - 可替换 github 镜像源，原先的 kgithub.com 可能出现无法请求的问题
>
> 2023-02-13 v1.0.3
> - 重构插件目录结构
> - 优化原有功能实现：干员信息、公招查询、理智提醒、塞壬点歌 [@issue/19](https://github.com/NumberSir/nonebot_plugin_arktools/issues/19) [@issue/21](https://github.com/NumberSir/nonebot_plugin_arktools/issues/21)
>   - 公招查询的截图识别改为 [百度 OCR](https://ai.baidu.com/tech/ocr) (腾讯 OCR 太拉了，识别不出烫金的高资和资深)
>   - 换用 [tortoise-orm](https://github.com/tortoise/tortoise-orm) 进行本地数据库异步读写
>   - 优化联网请求资源时的效率
> - 添加新功能：猜干员、今日干员、帮助图片
> - 最低支持 Python 版本上调至 Python3.8，与 Nonebot2-rc2 一致
> 
> 2022-09-27 v0.5.8
> - 修复理智恢复提醒文件检测不存在问题[@issue/16](https://github.com/NumberSir/nonebot_plugin_arktools/issues/16)
> - 重新添加文字公招查询[@issue/17](https://github.com/NumberSir/nonebot_plugin_arktools/issues/17)[@issue/18](https://github.com/NumberSir/nonebot_plugin_arktools/issues/18)
> - 优化干员查询：干员不存在时提醒
> - 优化公招查询：反馈检测到的公招标签
> 
> 2022-09-24 v0.5.7
> - 修复干员公招查询算法问题[@issue/13](https://github.com/NumberSir/nonebot_plugin_arktools/issues/13)
> - 修复干员公招查询作图重叠问题
> - 修复文件不存在报错问题[@issue/15](https://github.com/NumberSir/nonebot_plugin_arktools/issues/15)
> - 优化公招查询结果
> 
> 2022-09-23 v0.5.6
> - 干员查询添加模组材料查询
> 
> 2022-09-15 v0.5.5
> - 修复了json文件不会覆盖下载的问题
> - 修复了公招识别读取头像路径的问题[@issue/11](https://github.com/NumberSir/nonebot_plugin_arktools/issues/11)
> 
> 2022-09-01 v0.5.4
> - 修改资源获取方式为启动 nonebot 后下载到本地
> - 修复了检测路径缺失的问题[@issue/8](https://github.com/NumberSir/nonebot_plugin_arktools/issues/8)
>
> 2022-09-01 v0.5.3
> - 修复未导入 os 模块的问题
>
> 2022-09-01 v0.5.2
> - 修复公招保存图片出错和缺少文件的问题[@issue/7](https://github.com/NumberSir/nonebot_plugin_arktools/issues/7)
>
> 2022-09-01 v0.5.1
> - 重写了查询推荐公招标签的功能[@issue/6](https://github.com/NumberSir/nonebot_plugin_arktools/issues/6)
>
> 2022-08-29 v0.5.0
> - 添加了查询干员的技能升级材料、专精材料、精英化材料的功能
>
> 2022-06-03 v0.4.1
> - 修复了发行版和源码不匹配的问题[@issue/4](https://github.com/NumberSir/nonebot_plugin_arktools/issues/4)
> 
> 2022-06-03 v0.4.0
> - 添加了查询推荐公招标签的功能
>
> 2022-05-30 v0.3.0
> - 向下兼容到 Python 3.7.3 版本[@issue/2](https://github.com/NumberSir/nonebot_plugin_arktools/issues/2)
>
> 2022-05-30 v0.2.1
> - 修复了使用 nb plugin install 命令安装后无法正常工作的问题[@issue/1](https://github.com/NumberSir/nonebot_plugin_arktools/issues/1)
> 
> 2022-05-26 v0.2.0
> - 添加了查询最新活动信息的功能
>
> 2022-05-24 v0.1.0
> - 添加了查询今日开放资源关卡的功能
