import configparser


class Config:
    def __init__(self):
        # 读取配置文件
        cf = configparser.ConfigParser()
        cf.read("/Users/dengrongguan/PycharmProjects/WXRobot/plugins/config.ini", encoding='UTF-8')
        self.wechat_name = cf.get("configuration", "wechat_name")
        self.morning_time = cf.get("configuration", "morning_time")
        self.launch_time = cf.get("configuration", "launch_time")
        self.dinner_time = cf.get("configuration", "dinner_time")
        self.str_list_good_morning = ''
        with open("/Users/dengrongguan/PycharmProjects/WXRobot/remind_sentence/good_morning.txt", "r", encoding='UTF-8') as f:
            self.str_list_good_morning = f.readlines()


if __name__ == '__main__':
    config = Config()
    print(config.wechat_name)
