"""非游戏数据，如用户理智恢复提醒的表"""
from tortoise import fields
from tortoise.models import Model


class UserSanityModel(Model):
    gid = fields.IntField(null=True)
    uid = fields.IntField(null=True)
    record_san = fields.IntField(null=True, default=0)
    notify_san = fields.IntField(null=True, default=135)
    record_time = fields.DatetimeField(null=True)
    notify_time = fields.DatetimeField(null=True)
    status = fields.BooleanField(null=True, default=False)

    class Meta:
        table = "uo_user_sanity"  # uo = UnOfficial


PLUGIN_SQLITE_MODEL_MODULE_NAME = __name__


__all__ = [
    "UserSanityModel",

    "PLUGIN_SQLITE_MODEL_MODULE_NAME"
]
