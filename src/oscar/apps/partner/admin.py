from django.contrib import admin

from oscar.core.loading import get_model

Partner = get_model('partner', 'Partner')
StockRecord = get_model('partner', 'StockRecord')


class StockRecordAdmin(admin.ModelAdmin):
    list_display = ('product', 'partner', 'partner_sku', 'price_excl_tax',
                    'cost_price', 'num_in_stock')
    list_filter = ('partner',)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'partner':
            kwargs['initial'] = request.user.partner.id
            return db_field.formfield(**kwargs)

        return super(StockRecordAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

class StockRecordInline(admin.StackedInline):
	model = StockRecord
	extra = 1
	min_num = 1

admin.site.register(Partner)
admin.site.register(StockRecord, StockRecordAdmin)
