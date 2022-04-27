# Config
import configparser
import os

encoding = 'utf-8'

sections = {
    'bot': ['token', 'name', 'anchors', 'god_mode', 'purge_interval', 'default_chance', 'spam_stickers'],
    'grammar': ['chain_len', 'sep', 'stop_word', 'max_wrds', 'max_msgs', 'endsen', 'garbage', 'garbage_entities'],
    'logging': ['level'],
    'updates': ['mode'],
    'media_checker': ['lifetime', 'messages'],
    'redis': ['host', 'port', 'db']
}


def getlist(self, section, option, type=str):
    return list(map(lambda o: type(o), config.get(section, option).split(',')))

configparser.ConfigParser.getlist = getlist

root_config = 'resources/main.cfg'
user_config = os.getenv('CONFIG_PATH', 'cfg/main.plain.cfg')
config = configparser.ConfigParser()
config.read(root_config, encoding=encoding)
config.read(user_config, encoding=encoding)

for section, options in sections.items():
    if not config.has_section(section):
        raise ValueError("Config is not valid! Section '{}' is missing!".format(section))
    for option in options:
        if not config.has_option(section, option):
            raise ValueError("Config is not valid! Option '{}' in section '{}' is missing!".format(option, section))


# IOC
from .redis_c import Redis
redis = Redis(config)

from .tokenizer import Tokenizer
tokenizer = Tokenizer()

from .repository import *
trigram_repository = TrigramRepository()
chance_repository = ChanceRepository()
media_repository = MediaRepository()
job_repository = JobRepository()

from .service import *
data_learner = DataLearner()
reply_generator = ReplyGenerator()
media_checker = MediaUniquenessChecker()
chat_purge_queue = ChatPurgeQueue()