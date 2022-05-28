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

### 编写中...
1. [ ] 可以查询某种资源在哪个关卡期望理智最低
2. [ ] 根据当前有的资源和需要的资源种类、数量测算最优推图计划
3. [ ] 查询某干员的基础数据：
   1. [ ] 给定等级、信赖、潜能下的基础面板
   2. [ ] 天赋、特性、技能
   3. [ ] 干员精英化、技能专精、解锁模组需要的材料
   4. [ ] 干员种族、势力、身高等基本个人信息
4. [ ] 定时提醒剿灭 / 蚀刻章 / 合约等活动过期
  1. [ ] 查询当期/下期活动的介绍、链接、类别(如SS、合约、主线等)
5. [ ] 

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
daily_levels_path="xxx"  # 每日资源关卡的截图文件在本地存储的路径
...
```

各配置项的含义如上。

### 指令

使用以下指令触发，需加上指令前缀

```
格式：指令 -> 含义

今日方舟资源       ->     查看今天开放的资源关卡
更新今日方舟资源    ->     手动更新今天开放的资源关卡

```

## 图片示例
<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/170721093-80c0598e-9cd8-4cf4-b666-9c0a8faacc1d.png" width="500" />
</div>
