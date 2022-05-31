# lol-loot-repeated-redemption
LOL国服通行证代币神话精萃多次兑换脚本

**目前支持西部魔影(2022)通行证**

- 原理：通过roit的lcu api进行兑换可以绕过国服的兑换次数检测
- 可能的问题：该兑换可能会在数据库层面上被回滚（如果兑换的神话精萃被使用，目前来说不会有影响）

# 使用方法
1. 配置好相关依赖 `pip install lcu_driver`
2. 登录LOL国服
3. 运行 `lcu.py` (或者[LCU.exe](https://github.com/U-rara/lol-loot-repeated-redemption/releases/download/%E8%A5%BF%E9%83%A8%E9%AD%94%E5%BD%B1(2022)/LCU.exe))，完成兑换 (需要代币数额>=2200)
