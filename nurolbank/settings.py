BOT_NAME = 'nurolbank'
SPIDER_MODULES = ['nurolbank.spiders']
NEWSPIDER_MODULE = 'nurolbank.spiders'
ROBOTSTXT_OBEY = True
LOG_LEVEL = 'WARNING'
ITEM_PIPELINES = {
   'nurolbank.pipelines.DatabasePipeline': 300,
}
