from ihome import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = create_app("develop")

manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)




@manager.command
def init_data():
    "init_data"
    db.drop_all()
    db.create_all()
    db.session.execute(
        "INSERT INTO `ih_area_info`(`name`) VALUES ('东城区'),('西城区'),('朝阳区'),('海淀区'),('昌平区'),('丰台区'),('房山区'),('通州区'),('顺义区'),('大兴区'),('怀柔区'),('平谷区'),('密云区'),('延庆区'),('石景山区');")
    db.session.execute(
        "INSERT INTO `ih_facility_info`(`name`) VALUES('无线网络'),('热水淋浴'),('空调'),('暖气'),('允许吸烟'),('饮水设备'),('牙具'),('香皂'),('拖鞋'),('手纸'),('毛巾'),('沐浴露、洗发露'),('冰箱'),('洗衣机'),('电梯'),('允许做饭'),('允许带宠物'),('允许聚会'),('门禁系统'),('停车位'),('有线网络'),('电视'),('浴缸');")
    db.session.commit()  # <--- solution!


if __name__ == "__main__":
    manager.run()
