<p align="center">
  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>
</p>

<div align="center">
  
# Nonebot_Plugin_ArkTools
  
_✨ 基于 OneBot 适配器的 [NoneBot2](https://v2.nonebot.dev/) 明日方舟小工具箱插件 ✨_
  
</div>

[![OSCS Status](https://www.oscs1024.com/platform/badge/NumberSir/nonebot_plugin_arktools.svg?size=small)](https://www.oscs1024.com/project/NumberSir/nonebot_plugin_arktools?ref=badge_small)

本人python小萌新，插件有不完善和可以改进之处欢迎各位多提pr和issue

## 功能
### 已实现：
1. [x] 可以查询今天开放的资源关卡
2. [x] 可以查询最新的活动信息
3. [x] 可以查询推荐的公招标签(截图识别)
<<<<<<< Updated upstream
4. [x] 可以查询干员的技能升级材料、专精材料、精英化材料
5. [x] 可以通过网易云音乐点歌塞壬唱片中的音乐
=======
4. [x] 可以查询干员的技能升级材料、专精材料、精英化材料、模组升级材料
>>>>>>> Stashed changes

### 编写中...
1. [ ] 可以查询某种资源在哪个关卡期望理智最低
2. [ ] 根据当前有的资源和需要的资源种类、数量测算最优推图计划
3. [ ] 查询某干员的基础数据：
   1. [ ] 给定等级、信赖、潜能下的基础面板
   2. [ ] 天赋、特性、技能
   3. [ ] 干员种族、势力、身高等基本个人信息
4. [ ] 定时提醒剿灭 / 蚀刻章 / 合约等活动过期

## 安装

- 使用 nb-cli

```
nb plugin install nonebot_plugin_arktools
```

- 使用 pip

```
pip install nonebot_plugin_arktools
```

## 如何使用

### 启动注意
 - 每次启动并连接到客户端后会从 __[yuanyan3060](https://github.com/yuanyan3060)__ 的 __[明日方舟常用素材库](https://github.com/yuanyan3060/Arknights-Bot-Resource)__ 下载使用插件必需的文本及图片资源到本地，已经下载过的文件不会重复下载。下载根据网络情况不同可能耗时 20~30 分钟不等
 - 每天凌晨 4:30 会自动检测素材是否需要更新，若有则会自动下载更新的素材
 - 如需手动更新，请用命令 __“更新方舟游戏数据”__ 进行更新
 - 如果自动下载失败，请手动下载发行版中的 __“`operator_info.zip`”__ 压缩文件，解压到 __“`nonebot_plugin_arktools/_data`”__ 文件夹下，正确放置的文件夹结构应为：
```txt
nonebot_plugin_arktools
├── _data
│   └── operator_info
│       ├── font
│       ├── image
│       └── json
├── _apis
├── ...
...
```

### .env 配置项

```ini
daily_levels_path="xxx"     # 每日资源关卡的截图文件在本地存储的路径
activities_img_path="xxx"   # 新活动的截图文件在本地存储的路径
activities_data_path="xxx"  # 新活动的数据文件在本地存储的路径
operator_save_path="xxx"    # 干员信息查询生成的图片文件在本地存储的路径
tencent_cloud_secret_id="xxx"  # 腾讯云开发者 SecretId，这两项在 https://console.cloud.tencent.com/cam/capi 可以创建并查询
tencent_cloud_secret_key="xxx"  # 腾讯云开发者 SecretKey，另需开通 OCR 服务，见 https://console.cloud.tencent.com/ocr/overview
recruitment_save_path="xxx"  # 公招查询结果图片缓存路径
...
```

各配置项的含义如上。

### 指令

使用以下指令触发，需加上指令前缀

```
格式：指令 -> 含义

方舟今日资源       ->    查看今天开放的资源关卡
更新方舟今日资源    ->    手动更新今天开放的资源关卡

方舟最新活动    ->    查看最新的活动相关信息

更新方舟游戏数据   ->   更新至最新的游戏素材，以便公招识别与干员查询使用

公招[图片]    ->    查询推荐的公招标签
回复公招图片：公招 -> 同上

干员 [干员名称] ->   查询干员的技能升级材料、专精材料、精英化材料

塞壬点歌 [歌名]  ->   以网易云音乐小卡片的形式发送歌曲（其实不是塞壬唱片的歌也可以）
```

## 图片示例
<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/170930067-8b80374b-a454-4920-bc41-a15137b86118.png" width="500" />
</div>
<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/170831808-5b1bc7b4-3bea-45f5-8565-cc8b5a8372e3.png" width="500" />
</div>

<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/187737788-6a44179a-e76d-4c3b-97a1-d95c1a9ca35b.png" width="500" />
</div>
<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/187737797-5eb85331-cf3d-449e-b404-4c86eda41613.png" width="500" />
</div>
<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/187737802-866139c4-a556-475e-9018-e35cf64b1f29.png" width="500" />
</div>

<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/187153116-5caa84db-05d2-4cb4-85a1-898c3e71444e.png" width="500" />
</div>

<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/190354714-c255aeae-a04b-465d-b23f-199c6b211b77.png" width="500" />
</div>


## 感谢
 - __[yuanyan3060](https://github.com/yuanyan3060)__ 的 __[明日方舟常用素材库](https://github.com/yuanyan3060/Arknights-Bot-Resource)__
 - __[Kengxxiao](https://github.com/Kengxxiao)__ 的 __[《明日方舟》游戏数据库](https://github.com/Kengxxiao/ArknightsGameData)__


## 更新日志
> 2022-09-23 v0.5.6
> - 干员查询添加模组材料查询
> - 
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
