<p align="center">
  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>
</p>

<div align="center">
  
# Nonebot_Plugin_ArkTools
  
_✨ 基于OneBot适配器的[NoneBot2](https://v2.nonebot.dev/)明日方舟小工具箱插件 ✨_
  
</div>

## 功能
### 已实现：
1. [x] 可以查询今天开放的资源关卡
2. [x] 可以查询最新的活动信息

### 编写中...
1. [ ] 可以查询某种资源在哪个关卡期望理智最低
2. [ ] 根据当前有的资源和需要的资源种类、数量测算最优推图计划
3. [ ] 查询某干员的基础数据：
   1. [ ] 给定等级、信赖、潜能下的基础面板
   2. [ ] 天赋、特性、技能
   3. [ ] 干员精英化、技能专精、解锁模组需要的材料
   4. [ ] 干员种族、势力、身高等基本个人信息
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

### .env 配置项

```ini
daily_levels_path="xxx"     # 每日资源关卡的截图文件在本地存储的路径
activities_img_path="xxx"   # 新活动的截图文件在本地存储的路径
activities_data_path="xxx"  # 新活动的数据文件在本地存储的路径
...
```

各配置项的含义如上。

### 指令

使用以下指令触发，需加上指令前缀

```
格式：指令 -> 含义

方舟今日资源       ->     查看今天开放的资源关卡
更新方舟今日资源    ->     手动更新今天开放的资源关卡（需要 SUPERUSER 权限）

方舟最新活动        ->     查看最新的活动相关信息
```

## 图片示例
<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/170930067-8b80374b-a454-4920-bc41-a15137b86118.png" width="500" />
</div>
<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/170831808-5b1bc7b4-3bea-45f5-8565-cc8b5a8372e3.png" width="500" />
</div>
