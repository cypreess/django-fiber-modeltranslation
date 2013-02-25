from modeltranslation.translator import translator, TranslationOptions
from fiber.models import Page, ContentItem

class ContentItemTranslationOptions(TranslationOptions):
    fields = ('name', 'content_markup', 'content_html', )

class PageTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(ContentItem, ContentItemTranslationOptions)
translator.register(Page, PageTranslationOptions)
