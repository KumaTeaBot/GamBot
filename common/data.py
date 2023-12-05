from common.info import *

try:
    from local_db import trusted_group, bl_users
except ImportError:
    trusted_group = []
    bl_users = []


# stock

STOCK_DATA_PATH = 'data/stock'
STOCK_DATA_SUMMARY = 'summary.txt'
STOCK_DATA_UPDOWN = 'updown.txt'
STOCK_DATA_PRICE_IMG = 'image.txt'  # we are saving photo id

SINA_HEADER = {
    'Referer': 'https://finance.sina.com.cn/realstock/company/sh000001/nc.shtml'
}

STOCK_PRICE_API = 'https://hq.sinajs.cn/list={STOCK_CODE}'

STOCK_PRICE_IMG = 'https://image.sinajs.cn/newchart/min/n/{STOCK_CODE}.gif'
# daily: https://image.sinajs.cn/newchart/daily/n/sh000001.gif
# weekly: https://image.sinajs.cn/newchart/weekly/n/sh000001.gif
# monthly: https://image.sinajs.cn/newchart/monthly/n/sh000001.gif
# backup: https://webquotepic.eastmoney.com/GetPic.aspx?imageType=r&nid=1.000001
STOCK_PRICE_SMALL_IMG = 'https://image.sinajs.cn/newchart/hollow/small/nsh000001.gif'

UPDOWN_API = 'https://hq.sinajs.cn/list=sh000002_zdp,sz399107_zdp,sh000003_zdp,sz399108_zdp,sz399102_zdp'
UP_ICON = '🔴'
DOWN_ICON = '🟢'
STILL_ICON = '⚪'
RISE_ICON = '🔼'
FALL_ICON = '🔽'


# gacha

LOADING_DEFAULT = 'AgACAgUAAxkBAAMGZW8yOiTRz6gW2CvtXOn4eTqqit8AAi68MRvj_XlXULp0igotjbgACAEAAwIAA3gABx4E'

# # genshin
GACHA_GENSHIN_CMD = ['genshin', 'yuanshen', '原神', 'gs', 'ys', 'gi']
LOADING_GENSHIN = 'AgACAgUAAxkBAAMIZW8yh3HdhNmpzgnc8nczPGZeeq8AApe7MRtbkHhXEJyXoUvTpHoACAEAAwIAA3kABx4E'

# # arknights
GACHA_ARKNIGHTS_CMD = ['arknights', '方舟', '明日方舟', 'ark', 'mrfz', 'fz']
LOADING_ARKNIGHTS = 'AgACAgUAAxkBAAMKZW8yztd5Nux3qoyXotgaTjFapkgAApm7MRtbkHhXIHKInNaQDMoACAEAAwIAA3kABx4E'

# # groupmem
USER_PHOTO_DIR = 'data/groupmem'
USER_PHOTO_FILE = 'photo.p'
GACHA_GROUPMEM_CMD = ['groupmem', '群老婆', 'qlp', 'lp', 'group']
