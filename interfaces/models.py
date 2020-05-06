# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class AccountAccount(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    internal_type = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    deprecated = models.BooleanField(blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True, related_name='currency%(app_label)s_%(class)s_related')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name='company%(app_label)s_%(class)s_related')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    note = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=64)
    write_date = models.DateTimeField(blank=True, null=True)
    user_type = models.ForeignKey('AccountAccountType', models.DO_NOTHING, related_name='usertype%(app_label)s_%(class)s_related')
    last_time_entries_checked = models.DateTimeField(blank=True, null=True)
    reconcile = models.BooleanField(blank=True, null=True)
    afip_activity = models.ForeignKey('AfipActivity', models.DO_NOTHING, blank=True, null=True, related_name='afip_activity%(app_label)s_%(class)s_related')
    vat_f2002_category = models.ForeignKey('AfipVatF2002Category', models.DO_NOTHING, blank=True, null=True, related_name='vat_f2002_category%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'account_account'
        unique_together = (('code', 'company'),)


class AccountAccountAccountTag(models.Model):
    account_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, related_name='account_account%(app_label)s_%(class)s_related')
    account_account_tag = models.ForeignKey('AccountAccountTag', models.DO_NOTHING, related_name='account_account_tag%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'account_account_account_tag'
        unique_together = (('account_account', 'account_account_tag'),)


class AccountAccountFinancialReport(models.Model):
    report_line = models.ForeignKey('AccountFinancialReport', models.DO_NOTHING,related_name='report_line%(app_label)s_%(class)s_related')
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING, related_name='account%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'account_account_financial_report'
        unique_together = (('report_line', 'account'),)


class AccountAccountFinancialReportType(models.Model):
    report = models.ForeignKey('AccountFinancialReport', models.DO_NOTHING)
    account_type = models.ForeignKey('AccountAccountType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_financial_report_type'
        unique_together = (('report', 'account_type'),)


class AccountAccountTag(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    applicability = models.CharField(max_length=20)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    color = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    jurisdiction_code = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_account_tag'


class AccountAccountTagAccountTaxTemplateRel(models.Model):
    account_tax_template = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING)
    account_account_tag = models.ForeignKey(AccountAccountTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_tag_account_tax_template_rel'
        unique_together = (('account_tax_template', 'account_account_tag'),)


class AccountAccountTaxDefaultRel(models.Model):
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    tax = models.ForeignKey('AccountTax', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_tax_default_rel'
        unique_together = (('account', 'tax'),)


class AccountAccountTemplate(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    code = models.CharField(max_length=64)
    create_date = models.DateTimeField(blank=True, null=True)
    reconcile = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=20)
    chart_template = models.ForeignKey('AccountChartTemplate', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    nocreate = models.BooleanField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    user_type = models.ForeignKey('AccountAccountType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_template'


class AccountAccountTemplateAccountTag(models.Model):
    account_account_template = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING)
    account_account_tag = models.ForeignKey(AccountAccountTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_template_account_tag'
        unique_together = (('account_account_template', 'account_account_tag'),)


class AccountAccountTemplateTaxRel(models.Model):
    account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING)
    tax = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_template_tax_rel'
        unique_together = (('account', 'tax'),)


class AccountAccountType(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    note = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    include_initial_balance = models.BooleanField(blank=True, null=True)
    type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'account_account_type'


class AccountAccountTypeRel(models.Model):
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_type_rel'
        unique_together = (('journal', 'account'),)


class AccountAgedTrialBalance(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    period_length = models.IntegerField()
    date_from = models.DateField(blank=True, null=True)
    result_selection = models.CharField(max_length=20)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    target_move = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'account_aged_trial_balance'


class AccountAgedTrialBalanceAccountJournalRel(models.Model):
    account_aged_trial_balance = models.ForeignKey(AccountAgedTrialBalance, models.DO_NOTHING)
    account_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_aged_trial_balance_account_journal_rel'
        unique_together = (('account_aged_trial_balance', 'account_journal'),)


class AccountAnalyticAccount(models.Model):
    code = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    message_last_post = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    account_type = models.CharField(max_length=20)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    use_tasks = models.BooleanField(blank=True, null=True)
    recurring_invoicing_type = models.CharField(max_length=20, blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    recurring_invoices = models.BooleanField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True)
    pricelist = models.ForeignKey('Product_price_list', models.DO_NOTHING, blank=True, null=True)
    recurring_next_date = models.DateField(blank=True, null=True)
    recurring_interval = models.IntegerField(blank=True, null=True)
    recurring_rule_type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_account'


class AccountAnalyticAccountAccountInvoiceRel(models.Model):
    account_invoice = models.ForeignKey('AccountInvoice', models.DO_NOTHING)
    account_analytic_account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_analytic_account_account_invoice_rel'
        unique_together = (('account_invoice', 'account_analytic_account'),)


class AccountAnalyticAccountTagRel(models.Model):
    account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING)
    tag = models.ForeignKey('AccountAnalyticTag', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_analytic_account_tag_rel'
        unique_together = (('account', 'tag'),)


class AccountAnalyticChart(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_chart'


class AccountAnalyticInvoiceLine(models.Model):
    analytic_account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.TextField()
    discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_unit = models.FloatField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    uom = models.ForeignKey('ProductUom', models.DO_NOTHING)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    quantity = models.FloatField()

    class Meta:
        managed = False
        db_table = 'account_analytic_invoice_line'


class AccountAnalyticLine(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    unit_amount = models.FloatField(blank=True, null=True)
    date = models.DateField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=8, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    ref = models.CharField(max_length=20, blank=True, null=True)
    general_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    move = models.ForeignKey('AccountMoveLine', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True)
    product_uom = models.ForeignKey('ProductUom', models.DO_NOTHING, blank=True, null=True)
    amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    so_line = models.ForeignKey('SaleOrderLine', models.DO_NOTHING, db_column='so_line', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_line'


class AccountAnalyticLineTagRel(models.Model):
    line = models.ForeignKey(AccountAnalyticLine, models.DO_NOTHING)
    tag = models.ForeignKey('AccountAnalyticTag', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_analytic_line_tag_rel'
        unique_together = (('line', 'tag'),)


class AccountAnalyticTag(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    color = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_tag'


class AccountBalanceReport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    display_account = models.CharField(max_length=20)
    date_from = models.DateField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    target_move = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'account_balance_report'


class AccountBalanceReportJournalRel(models.Model):
    account = models.ForeignKey(AccountBalanceReport, models.DO_NOTHING)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_balance_report_journal_rel'
        unique_together = (('account', 'journal'),)


class AccountBankAccountsWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    bank_account = models.ForeignKey('WizardMultiChartsAccounts', models.DO_NOTHING)
    acc_name = models.CharField(max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    account_type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_bank_accounts_wizard'


class AccountBankStatement(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    date_done = models.DateTimeField(blank=True, null=True)
    balance_start = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)
    state = models.CharField(max_length=20)
    cashbox_start = models.ForeignKey('AccountBankStatementCashbox', models.DO_NOTHING, blank=True, null=True, related_name='cashbox_start%(app_label)s_%(class)s_related')
    cashbox_end = models.ForeignKey('AccountBankStatementCashbox', models.DO_NOTHING, blank=True, null=True)
    total_entry_encoding = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateField()
    difference = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    balance_end = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    balance_end_real = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_bank_statement'


class AccountBankStatementCashbox(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_bank_statement_cashbox'


class AccountBankStatementClosebalance(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'account_bank_statement_closebalance'


class AccountBankStatementImport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    data_file = models.BinaryField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_bank_statement_import'


class AccountBankStatementImportJournalCreation(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_bank_statement_import_journal_creation'


class AccountBankStatementLine(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    statement = models.ForeignKey(AccountBankStatement, models.DO_NOTHING)
    name = models.CharField(max_length=20)
    sequence = models.IntegerField(blank=True, null=True)
    partner_name = models.CharField(max_length=20, blank=True, null=True)
    ref = models.CharField(max_length=20, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    bank_account = models.ForeignKey('ResPartnerBank', models.DO_NOTHING, blank=True, null=True)
    date = models.DateField()
    amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    unique_import_id = models.CharField(unique=True, max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_bank_statement_line'


class AccountCashboxLine(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    cashbox = models.ForeignKey(AccountBankStatementCashbox, models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    coin_value = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'account_cashbox_line'


class AccountChangeCurrency(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    currency_rate = models.FloatField()

    class Meta:
        managed = False
        db_table = 'account_change_currency'


class AccountChartTemplate(models.Model):
    bank_account_code_prefix = models.CharField(max_length=5, blank=True, null=True)
    cash_account_code_prefix = models.CharField(max_length=5, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    visible = models.BooleanField(blank=True, null=True)
    property_account_receivable = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True, related_name='property_account_receivable%(app_label)s_%(class)s_related')
    property_stock_valuation_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True, related_name='property_stock_valuation_account%(app_label)s_%(class)s_related')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    complete_tax_set = models.BooleanField(blank=True, null=True)
    property_stock_account_output_categ = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True,  related_name='property_stock_account_output_categ%(app_label)s_%(class)s_related')
    transfer_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, related_name='tranfer_account%(app_label)s_%(class)s_related')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    expense_currency_exchange_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True, related_name='expense_currency_exchange_account%(app_label)s_%(class)s_related')
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, related_name='parent%(app_label)s_%(class)s_related')
    property_account_income_categ = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True, related_name='property_account_income_categ%(app_label)s_%(class)s_related')
    property_stock_account_input_categ = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_account_income = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True, related_name='property_ccount_income%(app_label)s_%(class)s_related')
    property_account_expense_categ = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True, related_name='property_account_expense_categ%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    use_anglo_saxon = models.BooleanField(blank=True, null=True)
    code_digits = models.IntegerField()
    name = models.CharField(max_length=20)
    property_account_expense = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True, related_name='property_account_expense%(app_label)s_%(class)s_related')
    property_account_payable = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True, related_name='property_account_payable%(app_label)s_%(class)s_related')
    income_currency_exchange_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True, related_name='income_currency_exchange_account%(app_label)s_%(class)s_related')
    localization = models.CharField(max_length=20, blank=True, null=True)
    opening_clousure_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True, related_name='opening_clousure_account%(app_label)s_%(class)s_related')
    rejected_check_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True, related_name='rejected_check_account%(app_label)s_%(class)s_related')
    deferred_check_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True, related_name='deferred_check_account%(app_label)s_%(class)s_related')
    holding_check_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True, related_name='holding_check_account%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'account_chart_template'


class AccountCheck(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    checkbook = models.ForeignKey('AccountCheckbook', models.DO_NOTHING, blank=True, null=True)
    number = models.IntegerField()
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    issue_date = models.DateField()
    message_last_post = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=20)
    type = models.CharField(max_length=20, blank=True, null=True)
    owner_name = models.CharField(max_length=20, blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    name = models.CharField(max_length=20)
    bank = models.ForeignKey('ResBank', models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    owner_vat = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_check'


class AccountCheckAccountPaymentRel(models.Model):
    account_payment = models.ForeignKey('AccountPayment', models.DO_NOTHING)
    account_check = models.ForeignKey(AccountCheck, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_check_account_payment_rel'
        unique_together = (('account_payment', 'account_check'),)


class AccountCheckActionWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    action_type = models.CharField(max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'account_check_action_wizard'


class AccountCheckOperation(models.Model):
    origin = models.CharField(max_length=20, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    check_0 = models.ForeignKey(AccountCheck, models.DO_NOTHING)
    notes = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateField()
    operation = models.CharField(max_length=20)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_check_operation'


class AccountCheckbook(models.Model):
    issue_check_subtype = models.CharField(max_length=20)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    numerate_on_printing = models.BooleanField(blank=True, null=True)
    range_to = models.IntegerField(blank=True, null=True)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    report_template = models.ForeignKey('IrActReportXml', models.DO_NOTHING, db_column='report_template', blank=True, null=True)
    sequence = models.ForeignKey('IrSequence', models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    block_manual_number = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_checkbook'


class AccountCommonAccountReport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    display_account = models.CharField(max_length=20)
    date_from = models.DateField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    target_move = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'account_common_account_report'


class AccountCommonAccountReportAccountJournalRel(models.Model):
    account_common_account_report = models.ForeignKey(AccountCommonAccountReport, models.DO_NOTHING)
    account_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_common_account_report_account_journal_rel'
        unique_together = (('account_common_account_report', 'account_journal'),)


class AccountCommonPartnerReport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    result_selection = models.CharField(max_length=20)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    target_move = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'account_common_partner_report'


class AccountCommonPartnerReportAccountJournalRel(models.Model):
    account_common_partner_report = models.ForeignKey(AccountCommonPartnerReport, models.DO_NOTHING)
    account_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_common_partner_report_account_journal_rel'
        unique_together = (('account_common_partner_report', 'account_journal'),)


class AccountCommonReport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    target_move = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'account_common_report'


class AccountCommonReportAccountJournalRel(models.Model):
    account_common_report = models.ForeignKey(AccountCommonReport, models.DO_NOTHING)
    account_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_common_report_account_journal_rel'
        unique_together = (('account_common_report', 'account_journal'),)


class AccountConfigSettings(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    module_account_asset = models.BooleanField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    module_account_accountant = models.BooleanField(blank=True, null=True)
    module_account_plaid = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    complete_tax_set = models.BooleanField(blank=True, null=True)
    template_transfer_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    module_account_bank_statement_import_qif = models.BooleanField(blank=True, null=True)
    module_account_budget = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    group_multi_currency = models.BooleanField(blank=True, null=True)
    group_proforma_invoices = models.BooleanField(blank=True, null=True)
    has_chart_of_accounts = models.BooleanField(blank=True, null=True)
    has_default_company = models.BooleanField(blank=True, null=True)
    purchase_tax_rate = models.FloatField(blank=True, null=True)
    module_account_bank_statement_import_ofx = models.BooleanField(blank=True, null=True)
    default_purchase_tax = models.ForeignKey('AccountTax', models.DO_NOTHING, blank=True, null=True, related_name='default_purchase_tax%(app_label)s_%(class)s_related')
    group_analytic_accounting = models.BooleanField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sale_tax_rate = models.FloatField(blank=True, null=True)
    module_account_batch_deposit = models.BooleanField(blank=True, null=True)
    module_account_yodlee = models.BooleanField(blank=True, null=True)
    module_account_tax_cash_basis = models.BooleanField(blank=True, null=True)
    chart_template = models.ForeignKey(AccountChartTemplate, models.DO_NOTHING, blank=True, null=True)
    default_sale_tax = models.ForeignKey('AccountTax', models.DO_NOTHING, blank=True, null=True)
    sale_tax = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING, blank=True, null=True)
    module_account_sepa = models.BooleanField(blank=True, null=True)
    module_account_reports = models.BooleanField(blank=True, null=True)
    module_l10n_us_check_printing = models.BooleanField(blank=True, null=True)
    module_account_reports_followup = models.BooleanField(blank=True, null=True)
    purchase_tax = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING, blank=True, null=True, related_name='purchase_tax%(app_label)s_%(class)s_related')
    module_payment_paypal = models.BooleanField(blank=True, null=True)
    module_payment_buckaroo = models.BooleanField(blank=True, null=True)
    module_payment_adyen = models.BooleanField(blank=True, null=True)
    module_payment_ogone = models.BooleanField(blank=True, null=True)
    module_payment_transfer = models.BooleanField(blank=True, null=True)
    sale_use_documents = models.BooleanField(blank=True, null=True)
    purchase_use_documents = models.BooleanField(blank=True, null=True)
    group_analytic_account_for_sales = models.BooleanField(blank=True, null=True)
    group_analytic_account_for_purchases = models.BooleanField(blank=True, null=True)
    default_acquirer = models.ForeignKey('PaymentAcquirer', models.DO_NOTHING, db_column='default_acquirer', blank=True, null=True)
    group_choose_payment_type = models.BooleanField(blank=True, null=True)
    group_pay_now_vendor_invoices = models.BooleanField(blank=True, null=True)
    group_pay_now_customer_invoices = models.BooleanField(blank=True, null=True)
    group_account_use_financial_amounts = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_config_settings'


class AccountDebtReportWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    secondary_currency = models.BooleanField(blank=True, null=True)
    historical_full = models.BooleanField(blank=True, null=True)
    company_type = models.CharField(max_length=20, blank=True, null=True)
    show_invoice_detail = models.BooleanField(blank=True, null=True)
    result_selection = models.CharField(max_length=20)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    financial_amounts = models.BooleanField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_debt_report_wizard'


class AccountDocLetResponsabilityIssuerRel(models.Model):
    afip_responsability_type = models.ForeignKey('AfipResponsabilityType', models.DO_NOTHING)
    letter = models.ForeignKey('AccountDocumentLetter', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_doc_let_responsability_issuer_rel'
        unique_together = (('afip_responsability_type', 'letter'),)


class AccountDocLetResponsabilityReceptorRel(models.Model):
    afip_responsability_type = models.ForeignKey('AfipResponsabilityType', models.DO_NOTHING)
    letter = models.ForeignKey('AccountDocumentLetter', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_doc_let_responsability_receptor_rel'
        unique_together = (('afip_responsability_type', 'letter'),)


class AccountDocumentLetter(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    taxes_included = models.BooleanField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_document_letter'


class AccountDocumentLetterResponsabilityIssuerRel(models.Model):
    document_letter = models.ForeignKey(AccountDocumentLetter, models.DO_NOTHING)
    afip_responsability_type = models.ForeignKey('AfipResponsabilityType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_document_letter_responsability_issuer_rel'
        unique_together = (('document_letter', 'afip_responsability_type'),)


class AccountDocumentLetterResponsabilityReceptorRel(models.Model):
    document_letter = models.ForeignKey(AccountDocumentLetter, models.DO_NOTHING)
    afip_responsability_type = models.ForeignKey('AfipResponsabilityType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_document_letter_responsability_receptor_rel'
        unique_together = (('document_letter', 'afip_responsability_type'),)


class AccountDocumentType(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    internal_type = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    validator = models.ForeignKey('BaseValidator', models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField()
    localization = models.CharField(max_length=20, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    doc_code_prefix = models.CharField(max_length=20, blank=True, null=True)
    report_name = models.CharField(max_length=20, blank=True, null=True)
    taxes_included = models.BooleanField(blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    document_letter = models.ForeignKey(AccountDocumentLetter, models.DO_NOTHING, blank=True, null=True)
    purchase_cuit_required = models.BooleanField(blank=True, null=True)
    purchase_alicuots = models.CharField(max_length=20, blank=True, null=True)
    export_to_citi = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_document_type'


class AccountFinancialReport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    level = models.IntegerField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    style_overwrite = models.IntegerField(blank=True, null=True)
    sign = models.IntegerField()
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    account_report = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, related_name='account_report%(app_label)s_%(class)s_related')
    display_detail = models.CharField(max_length=20, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_financial_report'


class AccountFiscalPosition(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    country_group = models.ForeignKey('ResCountryGroup', models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    zip_to = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=20)
    sequence = models.IntegerField(blank=True, null=True)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    auto_apply = models.BooleanField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    note = models.TextField(blank=True, null=True)
    zip_from = models.IntegerField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    vat_required = models.BooleanField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    afip_code = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position'


class AccountFiscalPositionAccount(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    account_dest = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    account_src = models.ForeignKey(AccountAccount, models.DO_NOTHING, related_name='account_scr%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_account'
        unique_together = (('position', 'account_src', 'account_dest'),)


class AccountFiscalPositionAccountTemplate(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    position = models.ForeignKey('AccountFiscalPositionTemplate', models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    account_dest = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    account_src = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, related_name='account_scr%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_account_template'


class AccountFiscalPositionResCountryStateRel(models.Model):
    account_fiscal_position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING)
    res_country_state = models.ForeignKey('ResCountryState', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_res_country_state_rel'
        unique_together = (('account_fiscal_position', 'res_country_state'),)


class AccountFiscalPositionTax(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING)
    tax_src = models.ForeignKey('AccountTax', models.DO_NOTHING, related_name='tax_scr%(app_label)s_%(class)s_related')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    tax_dest = models.ForeignKey('AccountTax', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_tax'
        unique_together = (('position', 'tax_src', 'tax_dest'),)


class AccountFiscalPositionTaxTemplate(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    position = models.ForeignKey('AccountFiscalPositionTemplate', models.DO_NOTHING)
    tax_src = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    tax_dest = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING, blank=True, null=True, related_name='task_dest%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_tax_template'


class AccountFiscalPositionTemplate(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    chart_template = models.ForeignKey(AccountChartTemplate, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    note = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    country_group = models.ForeignKey('ResCountryGroup', models.DO_NOTHING, blank=True, null=True)
    zip_to = models.IntegerField(blank=True, null=True)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True)
    auto_apply = models.BooleanField(blank=True, null=True)
    zip_from = models.IntegerField(blank=True, null=True)
    afip_code = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_template'


class AccountFiscalPositionTemplateResCountryStateRel(models.Model):
    account_fiscal_position_template = models.ForeignKey(AccountFiscalPositionTemplate, models.DO_NOTHING)
    res_country_state = models.ForeignKey('ResCountryState', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_template_res_country_state_rel'
        unique_together = (('account_fiscal_position_template', 'res_country_state'),)


class AccountFullReconcile(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_full_reconcile'


class AccountInvoice(models.Model):
    comment = models.TextField(blank=True, null=True)
    date_due = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    reference = models.CharField(max_length=20, blank=True, null=True)
    reference_type = models.CharField(max_length=20)
    number = models.CharField(max_length=20, blank=True, null=True)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, related_name='journal%(app_label)s_%(class)s_related')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    amount_total_company_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name='partner%(app_label)s_%(class)s_related')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    amount_untaxed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    partner_bank = models.ForeignKey('ResPartnerBank', models.DO_NOTHING, blank=True, null=True)
    residual_company_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_total_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    amount_tax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    fiscal_position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    sent = models.BooleanField(blank=True, null=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    reconciled = models.BooleanField(blank=True, null=True)
    origin = models.CharField(max_length=20, blank=True, null=True)
    residual = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    move_name = models.CharField(max_length=20, blank=True, null=True)
    date_invoice = models.DateField(blank=True, null=True)
    payment_term = models.ForeignKey('AccountPaymentTerm', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    residual_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    move = models.ForeignKey('AccountMove', models.DO_NOTHING, blank=True, null=True)
    amount_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_untaxed_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    commercial_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    document_number = models.CharField(max_length=20, blank=True, null=True)
    document_type = models.ForeignKey(AccountDocumentType, models.DO_NOTHING, blank=True, null=True)
    journal_document_type = models.ForeignKey('AccountJournalDocumentType', models.DO_NOTHING, blank=True, null=True)
    afip_service_start = models.DateField(blank=True, null=True)
    currency_rate = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    afip_service_end = models.DateField(blank=True, null=True)
    afip_incoterm = models.ForeignKey('AfipIncoterm', models.DO_NOTHING, blank=True, null=True)
    state_0 = models.ForeignKey('ResCountryState', models.DO_NOTHING, db_column='state_id', blank=True, null=True)  # Field renamed because of name conflict.
    force_afip_concept = models.CharField(max_length=20, blank=True, null=True)
    rejected_check = models.ForeignKey(AccountCheck, models.DO_NOTHING, blank=True, null=True)
    team = models.ForeignKey('CrmTeam', models.DO_NOTHING, blank=True, null=True)
    purchase = models.ForeignKey('PurchaseOrder', models.DO_NOTHING, blank=True, null=True)
    incoterms = models.ForeignKey('StockIncoterms', models.DO_NOTHING, blank=True, null=True)
    contract = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    internal_notes = models.TextField(blank=True, null=True)
    splitted_invoice = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    splitter_invoice = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True,related_name='splitter_invoice%(app_label)s_%(class)s_related')
    pay_now_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True)
    afip_auth_mode = models.CharField(max_length=20, blank=True, null=True)
    afip_auth_verify_result = models.CharField(max_length=20, blank=True, null=True)
    afip_xml_request = models.TextField(blank=True, null=True)
    afip_xml_response = models.TextField(blank=True, null=True)
    afip_batch_number = models.IntegerField(blank=True, null=True)
    afip_message = models.TextField(blank=True, null=True)
    afip_auth_code = models.CharField(max_length=24, blank=True, null=True)
    afip_auth_code_due = models.DateField(blank=True, null=True)
    afip_auth_verify_observation = models.CharField(max_length=20, blank=True, null=True)
    afip_result = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_invoice'
        unique_together = (('number', 'company', 'journal', 'type'),)


class AccountInvoiceAccountMoveLineRel(models.Model):
    account_invoice = models.ForeignKey(AccountInvoice, models.DO_NOTHING)
    account_move_line = models.ForeignKey('AccountMoveLine', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_invoice_account_move_line_rel'
        unique_together = (('account_invoice', 'account_move_line'),)


class AccountInvoiceCancel(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'account_invoice_cancel'


class AccountInvoiceConfirm(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'account_invoice_confirm'


class AccountInvoiceLine(models.Model):
    origin = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535)
    price_subtotal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    uom = models.ForeignKey('ProductUom', models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    account_analytic = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    price_subtotal_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    name = models.TextField()
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True)
    invoice = models.ForeignKey(AccountInvoice, models.DO_NOTHING, blank=True, null=True)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535)
    purchase_line = models.ForeignKey('PurchaseOrderLine', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_invoice_line'


class AccountInvoiceLineTax(models.Model):
    invoice_line = models.ForeignKey(AccountInvoiceLine, models.DO_NOTHING)
    tax = models.ForeignKey('AccountTax', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_invoice_line_tax'
        unique_together = (('invoice_line', 'tax'),)


class AccountInvoicePaymentRel(models.Model):
    payment = models.ForeignKey('AccountPayment', models.DO_NOTHING)
    invoice = models.ForeignKey(AccountInvoice, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_invoice_payment_rel'
        unique_together = (('payment', 'invoice'),)


class AccountInvoiceRefund(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    filter_refund = models.CharField(max_length=20)
    create_date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    date_invoice = models.DateField()
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    invoice = models.ForeignKey(AccountInvoice, models.DO_NOTHING, blank=True, null=True)
    document_number = models.CharField(max_length=20, blank=True, null=True)
    journal_document_type = models.ForeignKey('AccountJournalDocumentType', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_invoice_refund'


class AccountInvoiceTax(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    name = models.CharField(max_length=20)
    sequence = models.IntegerField(blank=True, null=True)
    invoice = models.ForeignKey(AccountInvoice, models.DO_NOTHING, blank=True, null=True)
    manual = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    account_analytic = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    tax = models.ForeignKey('AccountTax', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_invoice_tax'


class AccountJournal(models.Model):
    code = models.CharField(max_length=5)
    create_date = models.DateTimeField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    at_least_one_inbound = models.BooleanField(blank=True, null=True)
    bank_statements_source = models.CharField(max_length=5, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    group_invoice_lines = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    bank_account = models.ForeignKey('ResPartnerBank', models.DO_NOTHING, blank=True, null=True)
    profit_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True, related_name='profit_account%(app_label)s_%(class)s_related')
    display_on_footer = models.BooleanField(blank=True, null=True)
    type = models.CharField(max_length=5)
    default_debit_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    show_on_dashboard = models.BooleanField(blank=True, null=True)
    default_credit_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True, related_name='default_credit_account%(app_label)s_%(class)s_related')
    sequence_0 = models.ForeignKey('IrSequence', models.DO_NOTHING, db_column='sequence_id')  # Field renamed because of name conflict.
    write_date = models.DateTimeField(blank=True, null=True)
    refund_sequence = models.ForeignKey('IrSequence', models.DO_NOTHING, blank=True, null=True, related_name='refund_sequence%(app_label)s_%(class)s_related')
    loss_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True, related_name='loss_account%(app_label)s_%(class)s_related')
    update_posted = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=20)
    at_least_one_outbound = models.BooleanField(blank=True, null=True)
    refund_sequence_0 = models.BooleanField(db_column='refund_sequence', blank=True, null=True)  # Field renamed because of name conflict.
    document_sequence_type = models.CharField(max_length=20, blank=True, null=True)
    use_documents = models.BooleanField(blank=True, null=True)
    point_of_sale_type = models.CharField(max_length=20, blank=True, null=True)
    point_of_sale_number = models.IntegerField(blank=True, null=True)
    afip_ws = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_journal'
        unique_together = (('code', 'name', 'company'),)


class AccountJournalAccountingReportRel(models.Model):
    accounting_report = models.ForeignKey('AccountingReport', models.DO_NOTHING)
    account_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_journal_accounting_report_rel'
        unique_together = (('accounting_report', 'account_journal'),)


class AccountJournalDocumentType(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    document_type = models.ForeignKey(AccountDocumentType, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    sequence_0 = models.ForeignKey('IrSequence', models.DO_NOTHING, db_column='sequence_id', blank=True, null=True)  # Field renamed because of name conflict.
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_journal_document_type'


class AccountJournalInboundPaymentMethodRel(models.Model):
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    inbound_payment_method = models.ForeignKey('AccountPaymentMethod', models.DO_NOTHING, db_column='inbound_payment_method')

    class Meta:
        managed = False
        db_table = 'account_journal_inbound_payment_method_rel'
        unique_together = (('journal', 'inbound_payment_method'),)


class AccountJournalMergeWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    delete_from_journal = models.BooleanField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    from_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    to_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, related_name='to_journal%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'account_journal_merge_wizard'


class AccountJournalOutboundPaymentMethodRel(models.Model):
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    outbound_payment_method = models.ForeignKey('AccountPaymentMethod', models.DO_NOTHING, db_column='outbound_payment_method')

    class Meta:
        managed = False
        db_table = 'account_journal_outbound_payment_method_rel'
        unique_together = (('journal', 'outbound_payment_method'),)


class AccountJournalTypeRel(models.Model):
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    type = models.ForeignKey(AccountAccountType, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_journal_type_rel'
        unique_together = (('journal', 'type'),)


class AccountMove(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    statement_line = models.ForeignKey(AccountBankStatementLine, models.DO_NOTHING, blank=True, null=True)
    ref = models.CharField(max_length=20, blank=True, null=True)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=20)
    rate_diff_partial_rec = models.ForeignKey('AccountPartialReconcile', models.DO_NOTHING, blank=True, null=True)
    matched_percentage = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    narration = models.TextField(blank=True, null=True)
    date = models.DateField()
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=20)
    display_name = models.CharField(max_length=20, blank=True, null=True)
    document_number = models.CharField(max_length=20, blank=True, null=True)
    document_type = models.ForeignKey(AccountDocumentType, models.DO_NOTHING, blank=True, null=True)
    afip_responsability_type = models.ForeignKey('AfipResponsabilityType', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_move'


class AccountMoveLine(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    statement = models.ForeignKey(AccountBankStatement, models.DO_NOTHING, blank=True, null=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True, related_name='currency%(app_label)s_%(class)s_related')
    date_maturity = models.DateField()
    user_type = models.ForeignKey(AccountAccountType, models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    blocked = models.BooleanField(blank=True, null=True)
    analytic_account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    amount_residual = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    amount_residual_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    debit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ref = models.CharField(max_length=20, blank=True, null=True)
    debit_cash_basis = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    reconciled = models.BooleanField(blank=True, null=True)
    credit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    balance_cash_basis = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    move = models.ForeignKey(AccountMove, models.DO_NOTHING)
    name = models.CharField(max_length=20)
    payment = models.ForeignKey('AccountPayment', models.DO_NOTHING, blank=True, null=True)
    company_currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True)
    invoice = models.ForeignKey(AccountInvoice, models.DO_NOTHING, blank=True, null=True)
    tax_line = models.ForeignKey('AccountTax', models.DO_NOTHING, blank=True, null=True)
    credit_cash_basis = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product_uom = models.ForeignKey('ProductUom', models.DO_NOTHING, blank=True, null=True)
    amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    balance = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    full_reconcile = models.ForeignKey(AccountFullReconcile, models.DO_NOTHING, blank=True, null=True)
    document_type = models.ForeignKey(AccountDocumentType, models.DO_NOTHING, blank=True, null=True)
    afip_responsability_type = models.ForeignKey('AfipResponsabilityType', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_move_line'


class AccountMoveLineAccountTaxRel(models.Model):
    account_move_line = models.ForeignKey(AccountMoveLine, models.DO_NOTHING)
    account_tax = models.ForeignKey('AccountTax', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_move_line_account_tax_rel'
        unique_together = (('account_move_line', 'account_tax'),)


class AccountMoveLinePaymentGroupToPayRel(models.Model):
    payment_group = models.ForeignKey('AccountPaymentGroup', models.DO_NOTHING)
    to_pay_line = models.ForeignKey(AccountMoveLine, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_move_line_payment_group_to_pay_rel'
        unique_together = (('payment_group', 'to_pay_line'),)


class AccountMoveLineReconcile(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    writeoff = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    credit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    debit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    trans_nbr = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_move_line_reconcile'


class AccountMoveLineReconcileWriteoff(models.Model):
    comment = models.CharField(max_length=20)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    writeoff_acc = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    analytic = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_p = models.DateField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'account_move_line_reconcile_writeoff'


class AccountMoveReversal(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'account_move_reversal'


class AccountOperationTemplate(models.Model):
    second_analytic_account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    sequence = models.IntegerField()
    second_amount_type = models.CharField(max_length=20)
    second_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    analytic_account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True, related_name='analytic_account%(app_label)s_%(class)s_related')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    second_tax = models.ForeignKey('AccountTax', models.DO_NOTHING, blank=True, null=True)
    has_second_line = models.BooleanField(blank=True, null=True)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True, related_name='journal%(app_label)s_%(class)s_related')
    label = models.CharField(max_length=20, blank=True, null=True)
    second_label = models.CharField(max_length=20, blank=True, null=True)
    second_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True, related_name='account%(app_label)s_%(class)s_related')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    tax = models.ForeignKey('AccountTax', models.DO_NOTHING, blank=True, null=True, related_name='tax%(app_label)s_%(class)s_related')
    amount_type = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    second_amount = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'account_operation_template'


class AccountPartialReconcile(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    credit_move = models.ForeignKey(AccountMoveLine, models.DO_NOTHING, related_name='credit_move%(app_label)s_%(class)s_related')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    debit_move = models.ForeignKey(AccountMoveLine, models.DO_NOTHING, related_name='debit_move%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    full_reconcile = models.ForeignKey(AccountFullReconcile, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_partial_reconcile'


class AccountPayment(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    communication = models.CharField(max_length=20, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    payment_method = models.ForeignKey('AccountPaymentMethod', models.DO_NOTHING)
    payment_date = models.DateField()
    payment_difference_handling = models.CharField(max_length=20, blank=True, null=True)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, related_name='journal%(app_label)s_%(class)s_related')
    state = models.CharField(max_length=20, blank=True, null=True)
    writeoff_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    partner_type = models.CharField(max_length=20, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    name = models.CharField(max_length=20, blank=True, null=True)
    destination_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True, related_name='destination_journal%(app_label)s_%(class)s_related')
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    payment_type = models.CharField(max_length=20)
    payment_reference = models.CharField(max_length=20, blank=True, null=True)
    receiptbook = models.ForeignKey('AccountPaymentReceiptbook', models.DO_NOTHING, blank=True, null=True)
    document_number = models.CharField(max_length=20, blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    checkbook = models.ForeignKey(AccountCheckbook, models.DO_NOTHING, blank=True, null=True)
    check_bank = models.ForeignKey('ResBank', models.DO_NOTHING, blank=True, null=True)
    check_name = models.CharField(max_length=20, blank=True, null=True)
    check_issue_date = models.DateField(blank=True, null=True)
    check_owner_vat = models.CharField(max_length=20, blank=True, null=True)
    check_payment_date = models.DateField(blank=True, null=True)
    check_number = models.IntegerField(blank=True, null=True)
    check_owner_name = models.CharField(max_length=20, blank=True, null=True)
    withholding_base_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    withholding_number = models.CharField(max_length=20, blank=True, null=True)
    tax_withholding = models.ForeignKey('AccountTax', models.DO_NOTHING, blank=True, null=True)
    payment_group = models.ForeignKey('AccountPaymentGroup', models.DO_NOTHING, blank=True, null=True)
    force_amount_company_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    withholding_non_taxable_minimum = models.FloatField(blank=True, null=True)
    withholdable_invoiced_amount = models.FloatField(blank=True, null=True)
    period_withholding_amount = models.FloatField(blank=True, null=True)
    withholdable_advanced_amount = models.FloatField(blank=True, null=True)
    accumulated_amount = models.FloatField(blank=True, null=True)
    computed_withholding_amount = models.FloatField(blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    withholding_non_taxable_amount = models.FloatField(blank=True, null=True)
    withholdable_base_amount = models.FloatField(blank=True, null=True)
    previous_withholding_amount = models.FloatField(blank=True, null=True)
    automatic = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_payment'


class AccountPaymentGroup(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    payment_date = models.DateField()
    communication = models.CharField(max_length=20, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    partner_type = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    unreconciled_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    receiptbook = models.ForeignKey('AccountPaymentReceiptbook', models.DO_NOTHING, blank=True, null=True)
    document_number = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    regimen_ganancias = models.ForeignKey('AfipTablaGananciasAlicuotasymontos', models.DO_NOTHING, blank=True, null=True)
    retencion_ganancias = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_payment_group'
        unique_together = (('document_number', 'receiptbook'),)


class AccountPaymentGroupInvoiceWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=20, blank=True, null=True)
    payment_group = models.ForeignKey(AccountPaymentGroup, models.DO_NOTHING)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    date_invoice = models.DateField()
    account_analytic = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    amount_total = models.DecimalField(max_digits=65535, decimal_places=65535)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING)
    document_number = models.CharField(max_length=20, blank=True, null=True)
    journal_document_type = models.ForeignKey(AccountJournalDocumentType, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_payment_group_invoice_wizard'


class AccountPaymentGroupInvoiceWizardAccountTaxRel(models.Model):
    account_payment_group_invoice_wizard = models.ForeignKey(AccountPaymentGroupInvoiceWizard, models.DO_NOTHING)
    account_tax = models.ForeignKey('AccountTax', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_payment_group_invoice_wizard_account_tax_rel'
        unique_together = (('account_payment_group_invoice_wizard', 'account_tax'),)


class AccountPaymentMethod(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    code = models.CharField(max_length=20)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    payment_type = models.CharField(max_length=20)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_payment_method'


class AccountPaymentReceiptbook(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    prefix = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=64)
    sequence = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    document_type = models.ForeignKey(AccountDocumentType, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    padding = models.IntegerField(blank=True, null=True)
    partner_type = models.CharField(max_length=20)
    sequence_0 = models.ForeignKey('IrSequence', models.DO_NOTHING, db_column='sequence_id', blank=True, null=True)  # Field renamed because of name conflict.
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    sequence_type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_payment_receiptbook'


class AccountPaymentTerm(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    note = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_payment_term'


class AccountPaymentTermLine(models.Model):
    payment = models.ForeignKey(AccountPaymentTerm, models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    option = models.CharField(max_length=20)
    sequence = models.IntegerField(blank=True, null=True)
    days = models.IntegerField()
    value = models.CharField(max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    value_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_payment_term_line'


class AccountRegisterPayments(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    payment_date = models.DateField()
    communication = models.CharField(max_length=20, blank=True, null=True)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    partner_type = models.CharField(max_length=20, blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    payment_type = models.CharField(max_length=20)
    write_date = models.DateTimeField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    payment_method = models.ForeignKey(AccountPaymentMethod, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_register_payments'


class AccountReportGeneralLedger(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    initial_balance = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    display_account = models.CharField(max_length=20)
    date_from = models.DateField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    sortby = models.CharField(max_length=20)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    target_move = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'account_report_general_ledger'


class AccountReportGeneralLedgerJournalRel(models.Model):
    account = models.ForeignKey(AccountReportGeneralLedger, models.DO_NOTHING)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_report_general_ledger_journal_rel'
        unique_together = (('account', 'journal'),)


class AccountTax(models.Model):
    amount_type = models.CharField(max_length=20)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=20)
    sequence = models.IntegerField()
    tax_group = models.ForeignKey('AccountTaxGroup', models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    type_tax_use = models.CharField(max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    analytic = models.BooleanField(blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    include_base_amount = models.BooleanField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    price_include = models.BooleanField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    refund_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True, related_name='refund_account%(app_label)s_%(class)s_related')
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True, related_name='account%(app_label)s_%(class)s_related')
    withholding_sequence = models.ForeignKey('IrSequence', models.DO_NOTHING, blank=True, null=True)
    withholding_advances = models.BooleanField(blank=True, null=True)
    withholding_non_taxable_minimum = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    withholding_amount_type = models.CharField(max_length=20, blank=True, null=True)
    withholding_user_error_domain = models.CharField(max_length=20, blank=True, null=True)
    withholding_non_taxable_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    withholding_accumulated_payments = models.CharField(max_length=20, blank=True, null=True)
    withholding_user_error_message = models.CharField(max_length=20, blank=True, null=True)
    withholding_type = models.CharField(max_length=20)
    withholding_python_compute = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tax'
        unique_together = (('name', 'company', 'type_tax_use'),)


class AccountTaxAccountTag(models.Model):
    account_tax = models.ForeignKey(AccountTax, models.DO_NOTHING)
    account_account_tag = models.ForeignKey(AccountAccountTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_tax_account_tag'
        unique_together = (('account_tax', 'account_account_tag'),)


class AccountTaxFiliationRel(models.Model):
    parent_tax = models.ForeignKey(AccountTax, models.DO_NOTHING, db_column='parent_tax', related_name='parent_tax%(app_label)s_%(class)s_related')
    child_tax = models.ForeignKey(AccountTax, models.DO_NOTHING, db_column='child_tax', related_name='child_tax%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'account_tax_filiation_rel'
        unique_together = (('parent_tax', 'child_tax'),)


class AccountTaxGroup(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    sequence = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    tax = models.CharField(max_length=20, blank=True, null=True)
    afip_code = models.IntegerField(blank=True, null=True)
    application = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tax_group'


class AccountTaxPurchaseOrderLineRel(models.Model):
    purchase_order_line = models.ForeignKey('PurchaseOrderLine', models.DO_NOTHING)
    account_tax = models.ForeignKey(AccountTax, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_tax_purchase_order_line_rel'
        unique_together = (('purchase_order_line', 'account_tax'),)


class AccountTaxSaleAdvancePaymentInvRel(models.Model):
    sale_advance_payment_inv = models.ForeignKey('SaleAdvancePaymentInv', models.DO_NOTHING)
    account_tax = models.ForeignKey(AccountTax, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_tax_sale_advance_payment_inv_rel'
        unique_together = (('sale_advance_payment_inv', 'account_tax'),)


class AccountTaxSaleOrderLineRel(models.Model):
    sale_order_line = models.ForeignKey('SaleOrderLine', models.DO_NOTHING)
    account_tax = models.ForeignKey(AccountTax, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_tax_sale_order_line_rel'
        unique_together = (('sale_order_line', 'account_tax'),)


class AccountTaxTemplate(models.Model):
    amount_type = models.CharField(max_length=20)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=20)
    sequence = models.IntegerField()
    price_include = models.BooleanField(blank=True, null=True)
    chart_template = models.ForeignKey(AccountChartTemplate, models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    type_tax_use = models.CharField(max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    analytic = models.BooleanField(blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    include_base_amount = models.BooleanField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    refund_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True, related_name='refund_account%(app_label)s_%(class)s_related')
    account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True, related_name='account%(app_label)s_%(class)s_related')
    tax_group = models.ForeignKey(AccountTaxGroup, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tax_template'
        unique_together = (('name', 'company', 'type_tax_use'),)


class AccountTaxTemplateFiliationRel(models.Model):
    parent_tax = models.ForeignKey(AccountTaxTemplate, models.DO_NOTHING, db_column='parent_tax', related_name='parent_tax%(app_label)s_%(class)s_related')
    child_tax = models.ForeignKey(AccountTaxTemplate, models.DO_NOTHING, db_column='child_tax', related_name='child_tax%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'account_tax_template_filiation_rel'
        unique_together = (('parent_tax', 'child_tax'),)


class AccountTaxWithholdingRule(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    domain = models.CharField(max_length=20)
    create_date = models.DateTimeField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    fix_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    percentage = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tax_withholding = models.ForeignKey(AccountTax, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_tax_withholding_rule'


class AccountUnreconcile(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'account_unreconcile'


class AccountVatLedger(models.Model):
    presented_ledger = models.BinaryField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    reference = models.CharField(max_length=20, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    date_from = models.DateField()
    message_last_post = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    note = models.TextField(blank=True, null=True)
    first_page = models.IntegerField()
    state = models.CharField(max_length=20)
    presented_ledger_name = models.CharField(max_length=20, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField()
    last_page = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=20)
    sequence = models.IntegerField()
    reginfo_cv_cbte = models.TextField(db_column='REGINFO_CV_CBTE', blank=True, null=True)  # Field name made lowercase.
    tax_credit_computable_amount = models.FloatField(blank=True, null=True)
    prorate_type = models.CharField(max_length=20, blank=True, null=True)
    prorate_tax_credit = models.BooleanField(blank=True, null=True)
    reginfo_cv_cabecera = models.TextField(db_column='REGINFO_CV_CABECERA', blank=True, null=True)  # Field name made lowercase.
    reginfo_cv_alicuotas = models.TextField(db_column='REGINFO_CV_ALICUOTAS', blank=True, null=True)  # Field name made lowercase.
    reginfo_cv_compras_importaciones = models.TextField(db_column='REGINFO_CV_COMPRAS_IMPORTACIONES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'account_vat_ledger'


class AccountVatLedgerJournalRel(models.Model):
    vat_ledger = models.ForeignKey(AccountVatLedger, models.DO_NOTHING)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_vat_ledger_journal_rel'
        unique_together = (('vat_ledger', 'journal'),)


class AccountingReport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    date_to = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    filter_cmp = models.CharField(max_length=20)
    date_from = models.DateField(blank=True, null=True)
    enable_filter = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    date_to_cmp = models.DateField(blank=True, null=True)
    label_filter = models.CharField(max_length=20, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_from_cmp = models.DateField(blank=True, null=True)
    account_report = models.ForeignKey(AccountFinancialReport, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    debit_credit = models.BooleanField(blank=True, null=True)
    target_move = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'accounting_report'


class AerooAddPrintButton(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    state = models.CharField(max_length=20, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    open_action = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aeroo_add_print_button'


class AerooPrintActions(models.Model):
    out_format = models.CharField(max_length=20)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    copies = models.IntegerField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    out_format_code = models.CharField(max_length=16, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    report = models.ForeignKey('IrActReportXml', models.DO_NOTHING, blank=True, null=True)
    print_ids = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aeroo_print_actions'


class AerooPrintByAction(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    object_ids = models.CharField(max_length=250)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aeroo_print_by_action'


class AerooRemovePrintButton(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    state = models.CharField(max_length=20, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aeroo_remove_print_button'


class AerooReportImport(models.Model):
    info = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    state = models.CharField(max_length=20, blank=True, null=True)
    file = models.BinaryField()
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aeroo_report_import'


class AfipActivity(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    code = models.CharField(max_length=20)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'afip_activity'


class AfipConcept(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    code = models.CharField(max_length=20)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'afip_concept'


class AfipIncoterm(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    afip_code = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'afip_incoterm'


class AfipReponsbilityAccountFiscalPosRel(models.Model):
    position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING)
    afip_responsability_type = models.ForeignKey('AfipResponsabilityType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'afip_reponsbility_account_fiscal_pos_rel'
        unique_together = (('position', 'afip_responsability_type'),)


class AfipReponsbilityAccountFiscalPosTempRel(models.Model):
    position = models.ForeignKey(AccountFiscalPositionTemplate, models.DO_NOTHING)
    afip_responsability_type = models.ForeignKey('AfipResponsabilityType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'afip_reponsbility_account_fiscal_pos_temp_rel'
        unique_together = (('position', 'afip_responsability_type'),)


class AfipResponsabilityType(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='M')
    code = models.CharField(unique=True, max_length=8)
    name = models.CharField(unique=True, max_length=64)
    sequence = models.IntegerField(blank=True, null=True)
    company_requires_vat = models.BooleanField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        managed = False
        db_table = 'afip_responsability_type'


class AfipTablaGananciasAlicuotasymontos(models.Model):
    codigo_de_regimen = models.CharField(max_length=6)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    porcentaje_inscripto = models.FloatField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    concepto_referencia = models.TextField()
    write_date = models.DateTimeField(blank=True, null=True)
    anexo_referencia = models.CharField(max_length=20)
    porcentaje_no_inscripto = models.FloatField(blank=True, null=True)
    montos_no_sujetos_a_retencion = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'afip_tabla_ganancias_alicuotasymontos'


class AfipTablaGananciasEscala(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    importe_hasta = models.FloatField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    importe_excedente = models.FloatField(blank=True, null=True)
    importe_fijo = models.FloatField(blank=True, null=True)
    importe_desde = models.FloatField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    porcentaje = models.FloatField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'afip_tabla_ganancias_escala'


class AfipTax(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    code = models.CharField(max_length=20)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'afip_tax'


class AfipVatF2002Category(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'afip_vat_f2002_category'


class AfipWsConsultWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    number = models.IntegerField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'afip_ws_consult_wizard'


class AfipWsCurrencyRateWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'afip_ws_currency_rate_wizard'


class AfipWsfeError(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    code = models.CharField(max_length=2, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'afip_wsfe_error'


class AfipwsCertificate(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    crt = models.TextField(blank=True, null=True)
    alias = models.ForeignKey('AfipwsCertificateAlias', models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    state = models.CharField(max_length=20, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    csr = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'afipws_certificate'


class AfipwsCertificateAlias(models.Model):
    city = models.CharField(max_length=20)
    create_date = models.DateTimeField(blank=True, null=True)
    key = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    service_provider_cuit = models.CharField(max_length=16, blank=True, null=True)
    company_cuit = models.CharField(max_length=16, blank=True, null=True)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    common_name = models.CharField(max_length=64)
    state = models.CharField(max_length=20, blank=True, null=True)
    department = models.CharField(max_length=20)
    write_date = models.DateTimeField(blank=True, null=True)
    service_type = models.CharField(max_length=20)
    state_0 = models.ForeignKey('ResCountryState', models.DO_NOTHING, db_column='state_id', blank=True, null=True)  # Field renamed because of name conflict.
    type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'afipws_certificate_alias'


class AfipwsConnection(models.Model):
    afip_ws = models.CharField(max_length=20)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    generationtime = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    uniqueid = models.CharField(max_length=20, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    batch_sequence = models.ForeignKey('IrSequence', models.DO_NOTHING, blank=True, null=True)
    token = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    expirationtime = models.DateTimeField(blank=True, null=True)
    sign = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'afipws_connection'


class AfipwsUploadCertificateWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    certificate = models.ForeignKey(AfipwsCertificate, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    certificate_file = models.BinaryField()

    class Meta:
        managed = False
        db_table = 'afipws_upload_certificate_wizard'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BarcodeNomenclature(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=32)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    upc_ean_conv = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'barcode_nomenclature'


class BarcodeRule(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=32)
    sequence = models.IntegerField(blank=True, null=True)
    pattern = models.CharField(max_length=32)
    encoding = models.CharField(max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    alias = models.CharField(max_length=32)
    write_date = models.DateTimeField(blank=True, null=True)
    barcode_nomenclature = models.ForeignKey(BarcodeNomenclature, models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'barcode_rule'


class BaseActionRule(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    filter_pre = models.ForeignKey('IrFilters', models.DO_NOTHING, blank=True, null=True, related_name='filter_pre%(app_label)s_%(class)s_related')
    sequence = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    trg_date_range_type = models.CharField(max_length=20, blank=True, null=True)
    trg_date_range = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    filter_pre_domain = models.CharField(max_length=20, blank=True, null=True)
    on_change_fields = models.CharField(max_length=20, blank=True, null=True)
    filter = models.ForeignKey('IrFilters', models.DO_NOTHING, blank=True, null=True, related_name='filter%(app_label)s_%(class)s_related')
    model = models.ForeignKey('IrModel', models.DO_NOTHING)
    trg_date = models.ForeignKey('IrModelFields', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    kind = models.CharField(max_length=20, blank=True, null=True)
    filter_domain = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=20)
    act_user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    last_run = models.DateTimeField(blank=True, null=True)
    trg_date_calendar = models.ForeignKey('ResourceCalendar', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_action_rule'


class BaseActionRuleIrActServerRel(models.Model):
    base_action_rule = models.ForeignKey(BaseActionRule, models.DO_NOTHING)
    ir_act_server = models.ForeignKey('IrActServer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'base_action_rule_ir_act_server_rel'
        unique_together = (('base_action_rule', 'ir_act_server'),)


class BaseActionRuleLeadTest(models.Model):
    customer = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    date_action_last = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    priority = models.BooleanField(blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    deadline = models.BooleanField(blank=True, null=True)
    is_assigned_to_admin = models.BooleanField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_action_rule_lead_test'


class BaseActionRuleLineTest(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    lead = models.ForeignKey(BaseActionRuleLeadTest, models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_action_rule_line_test'


class BaseActionRuleResPartnerRel(models.Model):
    base_action_rule = models.ForeignKey(BaseActionRule, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'base_action_rule_res_partner_rel'
        unique_together = (('base_action_rule', 'res_partner'),)


class BaseConfigSettings(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    group_light_multi_company = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    module_google_drive = models.BooleanField(blank=True, null=True)
    module_inter_company_rules = models.BooleanField(blank=True, null=True)
    module_base_import = models.BooleanField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    module_portal = models.BooleanField(blank=True, null=True)
    module_google_calendar = models.BooleanField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    module_share = models.BooleanField(blank=True, null=True)
    module_auth_oauth = models.BooleanField(blank=True, null=True)
    company_share_partner = models.BooleanField(blank=True, null=True)
    fail_counter = models.IntegerField(blank=True, null=True)
    alias_domain = models.CharField(max_length=20, blank=True, null=True)
    auth_signup_reset_password = models.BooleanField(blank=True, null=True)
    auth_signup_uninvited = models.BooleanField(blank=True, null=True)
    auth_signup_template_user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    company_share_product = models.BooleanField(blank=True, null=True)
    group_product_variant = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_config_settings'


class BaseImportImport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    file_type = models.CharField(max_length=20, blank=True, null=True)
    file_name = models.CharField(max_length=20, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    file = models.BinaryField(blank=True, null=True)
    res_model = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_import'


class BaseImportTestsModelsChar(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.CharField(max_length=20, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char'


class BaseImportTestsModelsCharNoreadonly(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.CharField(max_length=20, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_noreadonly'


class BaseImportTestsModelsCharReadonly(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.CharField(max_length=20, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_readonly'


class BaseImportTestsModelsCharRequired(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.CharField(max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_required'


class BaseImportTestsModelsCharStates(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.CharField(max_length=20, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_states'


class BaseImportTestsModelsCharStillreadonly(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.CharField(max_length=20, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_stillreadonly'


class BaseImportTestsModelsM2O(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.ForeignKey('BaseImportTestsModelsM2ORelated', models.DO_NOTHING, db_column='value', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_m2o'


class BaseImportTestsModelsM2ORelated(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_m2o_related'


class BaseImportTestsModelsM2ORequired(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.ForeignKey('BaseImportTestsModelsM2ORequiredRelated', models.DO_NOTHING, db_column='value')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_m2o_required'


class BaseImportTestsModelsM2ORequiredRelated(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_m2o_required_related'


class BaseImportTestsModelsO2M(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_o2m'


class BaseImportTestsModelsO2MChild(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    parent = models.ForeignKey(BaseImportTestsModelsO2M, models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_o2m_child'


class BaseImportTestsModelsPreview(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    othervalue = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    somevalue = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_preview'


class BaseLanguageExport(models.Model):
    lang = models.CharField(max_length=20)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    format = models.CharField(max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    state = models.CharField(max_length=20, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    data = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_language_export'


class BaseLanguageImport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    code = models.CharField(max_length=5)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    filename = models.CharField(max_length=20)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    data = models.BinaryField()
    overwrite = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_language_import'


class BaseLanguageInstall(models.Model):
    lang = models.CharField(max_length=20)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    state = models.CharField(max_length=20, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    overwrite = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_language_install'


class BaseLanguageInstallWebsiteRel(models.Model):
    base_language_install = models.ForeignKey(BaseLanguageInstall, models.DO_NOTHING)
    website = models.ForeignKey('Website', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'base_language_install_website_rel'
        unique_together = (('base_language_install', 'website'),)


class BaseModuleConfiguration(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'base_module_configuration'


class BaseModuleUpdate(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    updated = models.IntegerField(blank=True, null=True)
    added = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    state = models.CharField(max_length=20, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_module_update'


class BaseModuleUpgrade(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    module_info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_module_upgrade'


class BasePartnerMergeAutomaticWizard(models.Model):
    exclude_journal_item = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    maximum_group = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    group_by_vat = models.BooleanField(blank=True, null=True)
    group_by_email = models.BooleanField(blank=True, null=True)
    group_by_parent_id = models.BooleanField(blank=True, null=True)
    exclude_contact = models.BooleanField(blank=True, null=True)
    group_by_is_company = models.BooleanField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    state = models.CharField(max_length=20)
    current_line = models.ForeignKey('BasePartnerMergeLine', models.DO_NOTHING, blank=True, null=True)
    group_by_name = models.BooleanField(blank=True, null=True)
    number_group = models.IntegerField(blank=True, null=True)
    dst_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_partner_merge_automatic_wizard'


class BasePartnerMergeAutomaticWizardResPartnerRel(models.Model):
    base_partner_merge_automatic_wizard = models.ForeignKey(BasePartnerMergeAutomaticWizard, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'base_partner_merge_automatic_wizard_res_partner_rel'
        unique_together = (('base_partner_merge_automatic_wizard', 'res_partner'),)


class BasePartnerMergeLine(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    aggr_ids = models.CharField(max_length=20)
    wizard = models.ForeignKey(BasePartnerMergeAutomaticWizard, models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    min_id = models.IntegerField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_partner_merge_line'


class BaseSetupTerminology(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    partner = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'base_setup_terminology'


class BaseUpdateTranslations(models.Model):
    lang = models.CharField(max_length=20)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_update_translations'


class BaseValidator(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    validation_code = models.TextField()
    write_date = models.DateTimeField(blank=True, null=True)
    input_test_string = models.CharField(max_length=20, blank=True, null=True)
    help_message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_validator'


class BusBus(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    message = models.CharField(max_length=20, blank=True, null=True)
    channel = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bus_bus'


class BusPresence(models.Model):
    status = models.CharField(max_length=20, blank=True, null=True)
    last_presence = models.DateTimeField(blank=True, null=True)
    user = models.OneToOneField('ResUsers', models.DO_NOTHING)
    last_poll = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bus_presence'


class CalendarAlarm(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    interval = models.CharField(max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    duration_minutes = models.IntegerField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    duration = models.IntegerField()
    type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'calendar_alarm'


class CalendarAlarmCalendarEventRel(models.Model):
    calendar_event = models.ForeignKey('CalendarEvent', models.DO_NOTHING)
    calendar_alarm = models.ForeignKey(CalendarAlarm, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'calendar_alarm_calendar_event_rel'
        unique_together = (('calendar_event', 'calendar_alarm'),)


class CalendarAttendee(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    cn = models.CharField(max_length=20, blank=True, null=True)
    access_token = models.CharField(max_length=20, blank=True, null=True)
    availability = models.CharField(max_length=20, blank=True, null=True)
    event = models.ForeignKey('CalendarEvent', models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    email = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar_attendee'


class CalendarContacts(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'calendar_contacts'


class CalendarEvent(models.Model):
    allday = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    display_start = models.CharField(max_length=20, blank=True, null=True)
    recurrency = models.BooleanField(blank=True, null=True)
    start_datetime = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    month_by = models.CharField(max_length=20, blank=True, null=True)
    rrule = models.CharField(max_length=20, blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    final_date = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    tu = models.BooleanField(blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    week_list = models.CharField(max_length=20, blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    start = models.DateTimeField()
    state = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=20, blank=True, null=True)
    th = models.BooleanField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    fr = models.BooleanField(blank=True, null=True)
    recurrent_id_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    stop_date = models.DateField(blank=True, null=True)
    stop = models.DateTimeField()
    stop_datetime = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    byday = models.CharField(max_length=20, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=20, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    count = models.IntegerField(blank=True, null=True)
    end_type = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=20)
    we = models.BooleanField(blank=True, null=True)
    mo = models.BooleanField(blank=True, null=True)
    interval = models.IntegerField(blank=True, null=True)
    su = models.BooleanField(blank=True, null=True)
    recurrent_id = models.IntegerField(blank=True, null=True)
    sa = models.BooleanField(blank=True, null=True)
    rrule_type = models.CharField(max_length=20, blank=True, null=True)
    show_as = models.CharField(max_length=20, blank=True, null=True)
    opportunity = models.ForeignKey('CrmLead', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar_event'


class CalendarEventResPartnerRel(models.Model):
    calendar_event = models.ForeignKey(CalendarEvent, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'calendar_event_res_partner_rel'
        unique_together = (('calendar_event', 'res_partner'),)


class CalendarEventType(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar_event_type'


class CashBoxIn(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    write_date = models.DateTimeField(blank=True, null=True)
    ref = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cash_box_in'


class CashBoxOut(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cash_box_out'


class ChangePasswordUser(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    user_login = models.CharField(max_length=20, blank=True, null=True)
    new_passwd = models.CharField(max_length=20, blank=True, null=True)
    wizard = models.ForeignKey('ChangePasswordWizard', models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'change_password_user'


class ChangePasswordWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'change_password_wizard'


class CrmActivity(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    days = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    activity_2 = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, related_name='activity_2%(app_label)s_%(class)s_related')
    activity_3 = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, related_name='activity_3%(app_label)s_%(class)s_related')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    team = models.ForeignKey('CrmTeam', models.DO_NOTHING, blank=True, null=True)
    subtype = models.ForeignKey('MailMessageSubtype', models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    activity_1 = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, related_name='activity_1%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'crm_activity'


class CrmLead(models.Model):
    date_closed = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    probability = models.FloatField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True)
    date_last_stage_update = models.DateTimeField(blank=True, null=True)
    date_action_last = models.DateTimeField(blank=True, null=True)
    campaign = models.ForeignKey('UtmCampaign', models.DO_NOTHING, blank=True, null=True)
    day_close = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    team = models.ForeignKey('CrmTeam', models.DO_NOTHING, blank=True, null=True)
    day_open = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    contact_name = models.CharField(max_length=64, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    date_action_next = models.DateTimeField(blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    date_conversion = models.DateTimeField(blank=True, null=True)
    opt_out = models.BooleanField(blank=True, null=True)
    date_open = models.DateTimeField(blank=True, null=True)
    title = models.ForeignKey('ResPartnerTitle', models.DO_NOTHING, db_column='title', blank=True, null=True)
    partner_name = models.CharField(max_length=64, blank=True, null=True)
    planned_revenue = models.FloatField(blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    priority = models.CharField(max_length=20, blank=True, null=True)
    next_activity = models.ForeignKey(CrmActivity, models.DO_NOTHING, blank=True, null=True, related_name='next_activity%(app_label)s_%(class)s_related')
    email_cc = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=20)
    function = models.CharField(max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    street2 = models.CharField(max_length=20, blank=True, null=True)
    date_deadline = models.DateField(blank=True, null=True)
    title_action = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    lost_reason = models.ForeignKey('CrmLostReason', models.DO_NOTHING, db_column='lost_reason', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    date_action = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=20)
    stage = models.ForeignKey('CrmStage', models.DO_NOTHING, blank=True, null=True)
    zip = models.CharField(max_length=24, blank=True, null=True)
    medium = models.ForeignKey('UtmMedium', models.DO_NOTHING, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    last_activity = models.ForeignKey(CrmActivity, models.DO_NOTHING, blank=True, null=True)
    street = models.CharField(max_length=20, blank=True, null=True)
    message_bounce = models.IntegerField(blank=True, null=True)
    source = models.ForeignKey('UtmSource', models.DO_NOTHING, blank=True, null=True)
    state = models.ForeignKey('ResCountryState', models.DO_NOTHING, blank=True, null=True)
    email_from = models.CharField(max_length=128, blank=True, null=True)
    referred = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_lead'


class CrmLead2OpportunityPartner(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=20)
    team = models.ForeignKey('CrmTeam', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    action = models.CharField(max_length=20)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_lead2opportunity_partner'


class CrmLead2OpportunityPartnerMass(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=20)
    force_assignation = models.BooleanField(blank=True, null=True)
    deduplicate = models.BooleanField(blank=True, null=True)
    team = models.ForeignKey('CrmTeam', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    action = models.CharField(max_length=20)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_lead2opportunity_partner_mass'


class CrmLead2OpportunityPartnerMassResUsersRel(models.Model):
    crm_lead2opportunity_partner_mass = models.ForeignKey(CrmLead2OpportunityPartnerMass, models.DO_NOTHING)
    res_users = models.ForeignKey('ResUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_lead2opportunity_partner_mass_res_users_rel'
        unique_together = (('crm_lead2opportunity_partner_mass', 'res_users'),)


class CrmLeadCrmLead2OpportunityPartnerMassRel(models.Model):
    crm_lead2opportunity_partner_mass = models.ForeignKey(CrmLead2OpportunityPartnerMass, models.DO_NOTHING)
    crm_lead = models.ForeignKey(CrmLead, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_lead_crm_lead2opportunity_partner_mass_rel'
        unique_together = (('crm_lead2opportunity_partner_mass', 'crm_lead'),)


class CrmLeadCrmLead2OpportunityPartnerRel(models.Model):
    crm_lead2opportunity_partner = models.ForeignKey(CrmLead2OpportunityPartner, models.DO_NOTHING)
    crm_lead = models.ForeignKey(CrmLead, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_lead_crm_lead2opportunity_partner_rel'
        unique_together = (('crm_lead2opportunity_partner', 'crm_lead'),)


class CrmLeadLost(models.Model):
    lost_reason = models.ForeignKey('CrmLostReason', models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    lead = models.ForeignKey(CrmLead, models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_lead_lost'


class CrmLeadTag(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=20)
    color = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    team = models.ForeignKey('CrmTeam', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_lead_tag'


class CrmLeadTagRel(models.Model):
    lead = models.ForeignKey(CrmLead, models.DO_NOTHING)
    tag = models.ForeignKey(CrmLeadTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_lead_tag_rel'
        unique_together = (('lead', 'tag'),)


class CrmLostReason(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_lost_reason'


class CrmMergeOpportunity(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    team = models.ForeignKey('CrmTeam', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'crm_merge_opportunity'


class CrmPartnerBinding(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    action = models.CharField(max_length=20)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_partner_binding'


class CrmStage(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    probability = models.FloatField()
    sequence = models.IntegerField(blank=True, null=True)
    on_change = models.BooleanField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    fold = models.BooleanField(blank=True, null=True)
    legend_priority = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'crm_stage'


class CrmTeam(models.Model):
    code = models.CharField(unique=True, max_length=8, blank=True, null=True)
    working_hours = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    name = models.CharField(max_length=64)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    color = models.IntegerField(blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    active = models.BooleanField(blank=True, null=True)
    reply_to = models.CharField(max_length=64, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    use_quotations = models.BooleanField(blank=True, null=True)
    invoiced_target = models.IntegerField(blank=True, null=True)
    use_invoices = models.BooleanField(blank=True, null=True)
    alias = models.ForeignKey('MailAlias', models.DO_NOTHING)
    use_leads = models.BooleanField(blank=True, null=True)
    use_opportunities = models.BooleanField(blank=True, null=True)
    resource_calendar = models.ForeignKey('ResourceCalendar', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_team'


class CrmTeamStageRel(models.Model):
    stage = models.ForeignKey(CrmStage, models.DO_NOTHING)
    team = models.ForeignKey(CrmTeam, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_team_stage_rel'
        unique_together = (('stage', 'team'),)


class CurrencyRateUpdateService(models.Model):
    next_run = models.DateField(blank=True, null=True)
    max_delta_days = models.IntegerField()
    create_date = models.DateTimeField(blank=True, null=True)
    service = models.CharField(max_length=20)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    interval_type = models.CharField(max_length=20, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    interval_number = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    rate_perc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    rate_surcharge = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'currency_rate_update_service'
        unique_together = (('service', 'company'),)


class DbBackup(models.Model):
    sftp_password = models.CharField(max_length=20, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=20, blank=True, null=True)
    sftp_user = models.CharField(max_length=20, blank=True, null=True)
    days_to_keep = models.IntegerField()
    message_last_post = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    method = models.CharField(max_length=20, blank=True, null=True)
    sftp_private_key = models.CharField(max_length=20, blank=True, null=True)
    sftp_host = models.CharField(max_length=20, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    folder = models.CharField(max_length=20)
    sftp_port = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'db_backup'


class DecimalPrecision(models.Model):
    digits = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'decimal_precision'


class DecimalPrecisionTest(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    float_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    float = models.FloatField(blank=True, null=True)
    float_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'decimal_precision_test'


class DeliveryCarrier(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    delivery_type = models.CharField(max_length=20)
    fixed_price = models.FloatField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    zip_to = models.CharField(max_length=20, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    amount = models.FloatField(blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING)
    shipping_enabled = models.BooleanField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    free_if_more_than = models.BooleanField(blank=True, null=True)
    zip_from = models.CharField(max_length=20, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'delivery_carrier'


class DeliveryCarrierCountryRel(models.Model):
    carrier = models.ForeignKey(DeliveryCarrier, models.DO_NOTHING)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'delivery_carrier_country_rel'
        unique_together = (('carrier', 'country'),)


class DeliveryCarrierStateRel(models.Model):
    carrier = models.ForeignKey(DeliveryCarrier, models.DO_NOTHING)
    state = models.ForeignKey('ResCountryState', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'delivery_carrier_state_rel'
        unique_together = (('carrier', 'state'),)


class DeliveryPriceRule(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    list_price = models.DecimalField(max_digits=65535, decimal_places=65535)
    sequence = models.IntegerField()
    max_value = models.FloatField()
    standard_price = models.DecimalField(max_digits=65535, decimal_places=65535)
    carrier = models.ForeignKey(DeliveryCarrier, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    list_base_price = models.DecimalField(max_digits=65535, decimal_places=65535)
    operator = models.CharField(max_length=20)
    variable_factor = models.CharField(max_length=20)
    write_date = models.DateTimeField(blank=True, null=True)
    variable = models.CharField(max_length=20)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'delivery_price_rule'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DocsConfigInstaller(models.Model):
    auth_type = models.CharField(max_length=20, blank=True, null=True)
    username = models.CharField(max_length=32, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    enabled = models.BooleanField(blank=True, null=True)
    host = models.CharField(max_length=64)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    state = models.CharField(max_length=20, blank=True, null=True)
    error_details = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    msg = models.TextField(blank=True, null=True)
    password = models.CharField(max_length=32, blank=True, null=True)
    port = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'docs_config_installer'


class EmailTemplateAttachmentRel(models.Model):
    email_template = models.ForeignKey('MailTemplate', models.DO_NOTHING)
    attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'email_template_attachment_rel'
        unique_together = (('email_template', 'attachment'),)


class EmailTemplatePreview(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    sub_object = models.ForeignKey('IrModel', models.DO_NOTHING, db_column='sub_object', blank=True, null=True, related_name='sub_object%(app_label)s_%(class)s_related')
    auto_delete = models.BooleanField(blank=True, null=True)
    mail_server = models.ForeignKey('IrMailServer', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    partner_to = models.CharField(max_length=20, blank=True, null=True)
    ref_ir_act_window = models.ForeignKey('IrActWindow', models.DO_NOTHING, db_column='ref_ir_act_window', blank=True, null=True)
    subject = models.CharField(max_length=20, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    report_template = models.ForeignKey('IrActReportXml', models.DO_NOTHING, db_column='report_template', blank=True, null=True)
    ref_ir_value = models.ForeignKey('IrValues', models.DO_NOTHING, db_column='ref_ir_value', blank=True, null=True)
    user_signature = models.BooleanField(blank=True, null=True)
    null_value = models.CharField(max_length=20, blank=True, null=True)
    email_cc = models.CharField(max_length=20, blank=True, null=True)
    res_id = models.CharField(max_length=20, blank=True, null=True)
    model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True, related_name='model%(app_label)s_%(class)s_related')
    sub_model_object_field = models.ForeignKey('IrModelFields', models.DO_NOTHING, db_column='sub_model_object_field', blank=True, null=True, related_name='sub_model%(app_label)s_%(class)s_related')
    body_html = models.TextField(blank=True, null=True)
    email_to = models.CharField(max_length=20, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    copyvalue = models.CharField(max_length=20, blank=True, null=True)
    lang = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    model_object_field = models.ForeignKey('IrModelFields', models.DO_NOTHING, db_column='model_object_field', blank=True, null=True)
    report_name = models.CharField(max_length=20, blank=True, null=True)
    use_default_to = models.BooleanField(blank=True, null=True)
    reply_to = models.CharField(max_length=20, blank=True, null=True)
    model_0 = models.CharField(db_column='model', max_length=20, blank=True, null=True)  # Field renamed because of name conflict.
    email_from = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_template_preview'


class EmailTemplatePreviewResPartnerRel(models.Model):
    email_template_preview = models.ForeignKey(EmailTemplatePreview, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'email_template_preview_res_partner_rel'
        unique_together = (('email_template_preview', 'res_partner'),)


class FetchmailConfigSettings(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'fetchmail_config_settings'


class FetchmailServer(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    configuration = models.TextField(blank=True, null=True)
    script = models.CharField(max_length=20, blank=True, null=True)
    object = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    attach = models.BooleanField(blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=20)
    action = models.ForeignKey('IrActServer', models.DO_NOTHING, blank=True, null=True)
    user = models.CharField(max_length=20, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=20)
    is_ssl = models.BooleanField(blank=True, null=True)
    server = models.CharField(max_length=20, blank=True, null=True)
    original = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fetchmail_server'


class Gateway(models.Model):
    nombre = models.CharField(max_length=100)
    pk_0 = models.BigIntegerField()
    direccion = models.CharField(max_length=100, blank=True, null=True)
    alta = models.CharField(max_length=10, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gateway'


class IrActClient(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    help = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    usage = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    res_model = models.CharField(max_length=20, blank=True, null=True)
    params_store = models.BinaryField(blank=True, null=True)
    tag = models.CharField(max_length=20)
    context = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'ir_act_client'


class IrActReportXml(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    help = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    usage = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    parser = models.CharField(max_length=20, blank=True, null=True)
    header = models.BooleanField(blank=True, null=True)
    report_type = models.CharField(max_length=20)
    ir_values = models.ForeignKey('IrValues', models.DO_NOTHING, blank=True, null=True)
    attachment = models.CharField(max_length=20, blank=True, null=True)
    report_sxw_content_data = models.BinaryField(blank=True, null=True)
    report_xml = models.CharField(max_length=20, blank=True, null=True)
    report_rml_content_data = models.BinaryField(blank=True, null=True)
    auto = models.BooleanField(blank=True, null=True)
    report_file = models.CharField(max_length=20, blank=True, null=True)
    multi = models.BooleanField(blank=True, null=True)
    report_xsl = models.CharField(max_length=20, blank=True, null=True)
    report_rml = models.CharField(max_length=20, blank=True, null=True)
    report_name = models.CharField(max_length=20)
    attachment_use = models.BooleanField(blank=True, null=True)
    model = models.CharField(max_length=20)
    paperformat = models.ForeignKey('ReportPaperformat', models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    logo = models.BinaryField(blank=True, null=True)
    background_image = models.BinaryField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    use_background_image = models.BooleanField(blank=True, null=True)
    print_logo = models.CharField(max_length=20)
    account_invoice_state = models.CharField(max_length=20, blank=True, null=True)
    account_invoice_lines_to_split = models.IntegerField(blank=True, null=True)
    payment_type = models.CharField(max_length=20, blank=True, null=True)
    account_invoice_split_invoice = models.BooleanField(blank=True, null=True)
    sale_order_state = models.CharField(max_length=20, blank=True, null=True)
    deferred_limit = models.IntegerField(blank=True, null=True)
    stylesheet = models.ForeignKey('ReportStylesheets', models.DO_NOTHING, blank=True, null=True)
    copies = models.IntegerField(blank=True, null=True)
    tml_source = models.CharField(max_length=20, blank=True, null=True)
    replace_report = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    out_format = models.ForeignKey('ReportMimetypes', models.DO_NOTHING, db_column='out_format', blank=True, null=True)
    deferred = models.CharField(max_length=20, blank=True, null=True)
    charset = models.CharField(max_length=20)
    parser_def = models.TextField(blank=True, null=True)
    preload_mode = models.CharField(max_length=20, blank=True, null=True)
    fallback_false = models.BooleanField(blank=True, null=True)
    parser_state = models.CharField(max_length=20, blank=True, null=True)
    styles_mode = models.CharField(max_length=20, blank=True, null=True)
    wizard = models.ForeignKey('IrActWindow', models.DO_NOTHING, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    report_wizard = models.BooleanField(blank=True, null=True)
    content_fname = models.CharField(max_length=64, blank=True, null=True)
    process_sep = models.BooleanField(blank=True, null=True)
    parser_loc = models.CharField(max_length=128, blank=True, null=True)
    copies_intercalate = models.BooleanField(blank=True, null=True)
    in_format = models.CharField(max_length=20, blank=True, null=True)
    download_filename = models.CharField(max_length=20, blank=True, null=True)
    partner_type = models.CharField(max_length=20, blank=True, null=True)
    stock_report_type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_act_report_xml'


class IrActServer(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    help = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    usage = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    code = models.TextField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    crud_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    condition = models.CharField(max_length=20, blank=True, null=True)
    ref_object = models.CharField(max_length=128, blank=True, null=True)
    id_object = models.CharField(max_length=128, blank=True, null=True)
    crud_model_name = models.CharField(max_length=20, blank=True, null=True)
    use_relational_model = models.CharField(max_length=20)
    use_create = models.CharField(max_length=20)
    wkf_field = models.ForeignKey('IrModelFields', models.DO_NOTHING, blank=True, null=True, related_name='wkf_field%(app_label)s_%(class)s_related')
    wkf_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True, related_name='wkf_model%(app_label)s_%(class)s_related')
    state = models.CharField(max_length=20)
    id_value = models.CharField(max_length=20, blank=True, null=True)
    action_id = models.IntegerField(blank=True, null=True)
    model = models.ForeignKey('IrModel', models.DO_NOTHING, related_name='model%(app_label)s_%(class)s_related')
    sub_model_object_field = models.ForeignKey('IrModelFields', models.DO_NOTHING, db_column='sub_model_object_field', blank=True, null=True, related_name='sub_model%(app_label)s_%(class)s_related')
    link_new_record = models.BooleanField(blank=True, null=True)
    wkf_transition = models.ForeignKey('WkfTransition', models.DO_NOTHING, blank=True, null=True)
    sub_object = models.ForeignKey('IrModel', models.DO_NOTHING, db_column='sub_object', blank=True, null=True, related_name='sub_object%(app_label)s_%(class)s_related')
    use_write = models.CharField(max_length=20)
    wkf_model_name = models.CharField(max_length=20, blank=True, null=True)
    copyvalue = models.CharField(max_length=20, blank=True, null=True)
    write_expression = models.CharField(max_length=20, blank=True, null=True)
    menu_ir_values = models.ForeignKey('IrValues', models.DO_NOTHING, blank=True, null=True)
    model_object_field = models.ForeignKey('IrModelFields', models.DO_NOTHING, db_column='model_object_field', blank=True, null=True)
    link_field = models.ForeignKey('IrModelFields', models.DO_NOTHING, blank=True, null=True, related_name='link_field%(app_label)s_%(class)s_related')
    template = models.ForeignKey('MailTemplate', models.DO_NOTHING, blank=True, null=True)
    website_published = models.BooleanField(blank=True, null=True)
    website_path = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_act_server'


class IrActUrl(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    help = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    usage = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    target = models.CharField(max_length=20)
    url = models.TextField()

    class Meta:
        managed = False
        db_table = 'ir_act_url'


class IrActWindow(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    help = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    usage = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    domain = models.CharField(max_length=20, blank=True, null=True)
    res_model = models.CharField(max_length=20)
    search_view = models.ForeignKey('IrUiView', models.DO_NOTHING, blank=True, null=True)
    view_type = models.CharField(max_length=20)
    src_model = models.CharField(max_length=20, blank=True, null=True)
    view = models.ForeignKey('IrUiView', models.DO_NOTHING, blank=True, null=True, related_name='view%(app_label)s_%(class)s_related')
    auto_refresh = models.IntegerField(blank=True, null=True)
    view_mode = models.CharField(max_length=20)
    target = models.CharField(max_length=20, blank=True, null=True)
    multi = models.BooleanField(blank=True, null=True)
    auto_search = models.BooleanField(blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    filter = models.BooleanField(blank=True, null=True)
    limit = models.IntegerField(blank=True, null=True)
    context = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'ir_act_window'


class IrActWindowGroupRel(models.Model):
    act = models.ForeignKey(IrActWindow, models.DO_NOTHING)
    gid = models.ForeignKey('ResGroups', models.DO_NOTHING, db_column='gid')

    class Meta:
        managed = False
        db_table = 'ir_act_window_group_rel'
        unique_together = (('act', 'gid'),)


class IrActWindowView(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    multi = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    view = models.ForeignKey('IrUiView', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    view_mode = models.CharField(max_length=20)
    write_date = models.DateTimeField(blank=True, null=True)
    act_window = models.ForeignKey(IrActWindow, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_act_window_view'
        unique_together = (('act_window', 'view_mode'),)


class IrActions(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    help = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    usage = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'ir_actions'


class IrActionsTodo(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    note = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=20)
    write_date = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=20)
    action_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ir_actions_todo'


class IrAttachment(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    res_model = models.CharField(max_length=20, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    res_name = models.CharField(max_length=20, blank=True, null=True)
    db_datas = models.BinaryField(blank=True, null=True)
    file_size = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    index_content = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=20)
    public = models.BooleanField(blank=True, null=True)
    store_fname = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    res_field = models.CharField(max_length=20, blank=True, null=True)
    mimetype = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=1024, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    checksum = models.CharField(max_length=40, blank=True, null=True)
    datas_fname = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_attachment'


class IrAutovacuum(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'ir_autovacuum'


class IrConfigParameter(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    value = models.TextField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    key = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'ir_config_parameter'


class IrConfigParameterGroupsRel(models.Model):
    icp = models.ForeignKey(IrConfigParameter, models.DO_NOTHING)
    group = models.ForeignKey('ResGroups', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ir_config_parameter_groups_rel'
        unique_together = (('icp', 'group'),)


class IrCron(models.Model):
    function = models.CharField(max_length=20, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    args = models.TextField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    name = models.CharField(max_length=20)
    interval_type = models.CharField(max_length=20, blank=True, null=True)
    numbercall = models.IntegerField(blank=True, null=True)
    nextcall = models.DateTimeField()
    priority = models.IntegerField(blank=True, null=True)
    model = models.CharField(max_length=20, blank=True, null=True)
    doall = models.BooleanField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    interval_number = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'ir_cron'


class IrExports(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    resource = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_exports'


class IrExportsLine(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    export = models.ForeignKey(IrExports, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_exports_line'


class IrFilters(models.Model):
    sort = models.TextField()
    model_id = models.CharField(max_length=20)
    domain = models.TextField()
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=20)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    is_default = models.BooleanField(blank=True, null=True)
    context = models.TextField()
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    action_id = models.IntegerField(blank=True, null=True)

    # A unique constraint could not be introspected.
    class Meta:
        managed = False
        db_table = 'ir_filters'
        unique_together = (('name', 'model_id', 'user', 'action_id'),)


class IrLogging(models.Model):
    create_uid = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    level = models.CharField(max_length=20, blank=True, null=True)
    line = models.CharField(max_length=20)
    dbname = models.CharField(max_length=20, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    func = models.CharField(max_length=20)
    write_date = models.DateTimeField(blank=True, null=True)
    path = models.CharField(max_length=20)
    message = models.TextField()
    type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'ir_logging'


class IrMailServer(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    smtp_encryption = models.CharField(max_length=20)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    sequence = models.IntegerField(blank=True, null=True)
    smtp_port = models.IntegerField()
    smtp_host = models.CharField(max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    smtp_pass = models.CharField(max_length=64, blank=True, null=True)
    smtp_debug = models.BooleanField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    smtp_user = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_mail_server'


class IrModel(models.Model):
    model = models.CharField(unique=True, max_length=20)
    name = models.CharField(max_length=20)
    state = models.CharField(max_length=20, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    transient = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model'


class IrModelAccess(models.Model):
    model = models.ForeignKey(IrModel, models.DO_NOTHING)
    perm_read = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=20)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    active = models.BooleanField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    perm_unlink = models.BooleanField(blank=True, null=True)
    perm_write = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    perm_create = models.BooleanField(blank=True, null=True)
    group = models.ForeignKey('ResGroups', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model_access'


class IrModelConstraint(models.Model):
    date_init = models.DateTimeField(blank=True, null=True)
    date_update = models.DateTimeField(blank=True, null=True)
    module = models.ForeignKey('IrModuleModule', models.DO_NOTHING, db_column='module')
    model = models.ForeignKey(IrModel, models.DO_NOTHING, db_column='model')
    type = models.CharField(max_length=1)
    definition = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=20)
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model_constraint'
        unique_together = (('name', 'module'),)


class IrModelData(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    noupdate = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=20)
    date_init = models.DateTimeField(blank=True, null=True)
    date_update = models.DateTimeField(blank=True, null=True)
    module = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    res_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model_data'
        unique_together = (('module', 'name'),)


class IrModelFields(models.Model):
    model = models.CharField(max_length=20)
    model_0 = models.ForeignKey(IrModel, models.DO_NOTHING, db_column='model_id')  # Field renamed because of name conflict.
    name = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    field_description = models.CharField(max_length=20)
    help = models.TextField(blank=True, null=True)
    ttype = models.CharField(max_length=20)
    relation = models.CharField(max_length=20, blank=True, null=True)
    relation_field = models.CharField(max_length=20, blank=True, null=True)
    index = models.BooleanField(blank=True, null=True)
    copy = models.BooleanField(blank=True, null=True)
    related = models.CharField(max_length=20, blank=True, null=True)
    readonly = models.BooleanField(blank=True, null=True)
    required = models.BooleanField(blank=True, null=True)
    selectable = models.BooleanField(blank=True, null=True)
    translate = models.BooleanField(blank=True, null=True)
    serialization_field = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    relation_table = models.CharField(max_length=20, blank=True, null=True)
    column1 = models.CharField(max_length=20, blank=True, null=True)
    column2 = models.CharField(max_length=20, blank=True, null=True)
    domain = models.CharField(max_length=20, blank=True, null=True)
    selection = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    on_delete = models.CharField(max_length=20, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    depends = models.CharField(max_length=20, blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    complete_name = models.CharField(max_length=20, blank=True, null=True)
    compute = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model_fields'


class IrModelFieldsGroupRel(models.Model):
    field = models.ForeignKey(IrModelFields, models.DO_NOTHING)
    group = models.ForeignKey('ResGroups', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ir_model_fields_group_rel'
        unique_together = (('field', 'group'),)


class IrModelRelation(models.Model):
    date_init = models.DateTimeField(blank=True, null=True)
    date_update = models.DateTimeField(blank=True, null=True)
    module = models.ForeignKey('IrModuleModule', models.DO_NOTHING, db_column='module')
    model = models.ForeignKey(IrModel, models.DO_NOTHING, db_column='model')
    name = models.CharField(max_length=20)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model_relation'


class IrModuleCategory(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    visible = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_module_category'


class IrModuleModule(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    website = models.CharField(max_length=20, blank=True, null=True)
    summary = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(unique=True, max_length=20)
    author = models.CharField(max_length=20, blank=True, null=True)
    icon = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    latest_version = models.CharField(max_length=20, blank=True, null=True)
    shortdesc = models.CharField(max_length=20, blank=True, null=True)
    category = models.ForeignKey(IrModuleCategory, models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    application = models.BooleanField(blank=True, null=True)
    demo = models.BooleanField(blank=True, null=True)
    web = models.BooleanField(blank=True, null=True)
    license = models.CharField(max_length=20, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    auto_install = models.BooleanField(blank=True, null=True)
    menus_by_module = models.TextField(blank=True, null=True)
    reports_by_module = models.TextField(blank=True, null=True)
    maintainer = models.CharField(max_length=20, blank=True, null=True)
    contributors = models.TextField(blank=True, null=True)
    views_by_module = models.TextField(blank=True, null=True)
    published_version = models.CharField(max_length=20, blank=True, null=True)
    url = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_module_module'


class IrModuleModuleDependency(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    name = models.CharField(max_length=20, blank=True, null=True)
    module = models.ForeignKey(IrModuleModule, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_module_module_dependency'


class IrProperty(models.Model):
    value_text = models.TextField(blank=True, null=True)
    value_float = models.FloatField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    type = models.CharField(max_length=20)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    fields = models.ForeignKey(IrModelFields, models.DO_NOTHING)
    value_datetime = models.DateTimeField(blank=True, null=True)
    value_binary = models.BinaryField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    value_reference = models.CharField(max_length=20, blank=True, null=True)
    value_integer = models.IntegerField(blank=True, null=True)
    res_id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_property'


class IrRule(models.Model):
    model = models.ForeignKey(IrModel, models.DO_NOTHING)
    domain_force = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    global_field = models.BooleanField(db_column='global', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    active = models.BooleanField(blank=True, null=True)
    perm_read = models.BooleanField(blank=True, null=True)
    perm_unlink = models.BooleanField(blank=True, null=True)
    perm_write = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    perm_create = models.BooleanField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_rule'


class IrSequence(models.Model):
    padding = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    code = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    number_next = models.IntegerField()
    implementation = models.CharField(max_length=20)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    use_date_range = models.BooleanField(blank=True, null=True)
    number_increment = models.IntegerField()
    prefix = models.CharField(max_length=20, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    suffix = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_sequence'


class IrSequenceDateRange(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    number_next = models.IntegerField()
    date_from = models.DateField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    sequence = models.ForeignKey(IrSequence, models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField()

    class Meta:
        managed = False
        db_table = 'ir_sequence_date_range'


class IrServerObjectLines(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    server = models.ForeignKey(IrActServer, models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.TextField()
    col1 = models.ForeignKey(IrModelFields, models.DO_NOTHING, db_column='col1')
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'ir_server_object_lines'


class IrTranslation(models.Model):
    lang = models.ForeignKey('ResLang', models.DO_NOTHING, db_column='lang', blank=True, null=True)
    src = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=20)
    res_id = models.IntegerField(blank=True, null=True)
    module = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_translation'


class IrUiMenu(models.Model):
    parent_left = models.IntegerField(blank=True, null=True)
    parent_right = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    web_icon = models.CharField(max_length=20, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    action = models.CharField(max_length=20, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'ir_ui_menu'


class IrUiMenuGroupRel(models.Model):
    menu = models.ForeignKey(IrUiMenu, models.DO_NOTHING)
    gid = models.ForeignKey('ResGroups', models.DO_NOTHING, db_column='gid')

    class Meta:
        managed = False
        db_table = 'ir_ui_menu_group_rel'
        unique_together = (('menu', 'gid'),)


class IrUiView(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    field_parent = models.CharField(max_length=20, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    model_data = models.ForeignKey(IrModelData, models.DO_NOTHING, blank=True, null=True)
    priority = models.IntegerField()
    type = models.CharField(max_length=20, blank=True, null=True)
    arch_db = models.TextField(blank=True, null=True)
    inherit = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    key = models.CharField(max_length=20, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    arch_fs = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=20)
    mode = models.CharField(max_length=20)
    model = models.CharField(max_length=20, blank=True, null=True)
    website = models.ForeignKey('Website', models.DO_NOTHING, blank=True, null=True)
    customize_show = models.BooleanField(blank=True, null=True)
    website_meta_title = models.CharField(max_length=20, blank=True, null=True)
    website_meta_description = models.TextField(blank=True, null=True)
    website_meta_keywords = models.CharField(max_length=20, blank=True, null=True)
    page = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_ui_view'


class IrUiViewCustom(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    ref = models.ForeignKey(IrUiView, models.DO_NOTHING)
    arch = models.TextField()

    class Meta:
        managed = False
        db_table = 'ir_ui_view_custom'


class IrUiViewGroupRel(models.Model):
    view = models.ForeignKey(IrUiView, models.DO_NOTHING)
    group = models.ForeignKey('ResGroups', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ir_ui_view_group_rel'
        unique_together = (('view', 'group'),)


class IrValues(models.Model):
    model = models.ForeignKey(IrModel, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=20)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    key2 = models.CharField(max_length=20, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    key = models.CharField(max_length=20)
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    model_0 = models.CharField(db_column='model', max_length=20)  # Field renamed because of name conflict.
    res_id = models.IntegerField(blank=True, null=True)
    action_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_values'


class LinkTracker(models.Model):
    count = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    medium = models.ForeignKey('UtmMedium', models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=20, blank=True, null=True)
    url = models.CharField(max_length=20)
    campaign = models.ForeignKey('UtmCampaign', models.DO_NOTHING, blank=True, null=True)
    favicon = models.CharField(max_length=20, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    source = models.ForeignKey('UtmSource', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    mass_mailing_campaign = models.ForeignKey('MailMassMailingCampaign', models.DO_NOTHING, blank=True, null=True)
    mass_mailing = models.ForeignKey('MailMassMailing', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'link_tracker'


class LinkTrackerClick(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    ip = models.CharField(max_length=20, blank=True, null=True)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True)
    link = models.ForeignKey(LinkTracker, models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    click_date = models.DateField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    mail_stat = models.ForeignKey('MailMailStatistics', models.DO_NOTHING, blank=True, null=True)
    mass_mailing_campaign = models.ForeignKey('MailMassMailingCampaign', models.DO_NOTHING, blank=True, null=True)
    mass_mailing = models.ForeignKey('MailMassMailing', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'link_tracker_click'


class LinkTrackerCode(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    code = models.CharField(unique=True, max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    link = models.ForeignKey(LinkTracker, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'link_tracker_code'


class MailAlias(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    alias_defaults = models.TextField()
    alias_contact = models.CharField(max_length=20)
    alias_parent_model = models.ForeignKey(IrModel, models.DO_NOTHING, blank=True, null=True, related_name='alias_parent_model%(app_label)s_%(class)s_related')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    alias_force_thread_id = models.IntegerField(blank=True, null=True)
    alias_model = models.ForeignKey(IrModel, models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    alias_parent_thread_id = models.IntegerField(blank=True, null=True)
    alias_user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    alias_name = models.CharField(unique=True, max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_alias'


class MailChannel(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    alias = models.ForeignKey(MailAlias, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    uuid = models.CharField(max_length=50, blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    public = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    group_public = models.ForeignKey('ResGroups', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    channel_type = models.CharField(max_length=20, blank=True, null=True)
    email_send = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_channel'


class MailChannelMailWizardInviteRel(models.Model):
    mail_wizard_invite = models.ForeignKey('MailWizardInvite', models.DO_NOTHING)
    mail_channel = models.ForeignKey(MailChannel, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_channel_mail_wizard_invite_rel'
        unique_together = (('mail_wizard_invite', 'mail_channel'),)


class MailChannelPartner(models.Model):
    seen_message = models.ForeignKey('MailMessage', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    is_minimized = models.BooleanField(blank=True, null=True)
    is_pinned = models.BooleanField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    channel = models.ForeignKey(MailChannel, models.DO_NOTHING, blank=True, null=True)
    fold_state = models.CharField(max_length=20, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_channel_partner'


class MailChannelResGroupRel(models.Model):
    mail_channel = models.ForeignKey(MailChannel, models.DO_NOTHING)
    groups = models.ForeignKey('ResGroups', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_channel_res_group_rel'
        unique_together = (('mail_channel', 'groups'),)


class MailComposeMessage(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    no_auto_thread = models.BooleanField(blank=True, null=True)
    mail_server = models.ForeignKey(IrMailServer, models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    notify = models.BooleanField(blank=True, null=True)
    active_domain = models.TextField(blank=True, null=True)
    subject = models.CharField(max_length=20, blank=True, null=True)
    composition_mode = models.CharField(max_length=20, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    is_log = models.BooleanField(blank=True, null=True)
    parent = models.ForeignKey('MailMessage', models.DO_NOTHING, blank=True, null=True)
    subtype = models.ForeignKey('MailMessageSubtype', models.DO_NOTHING, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    message_id = models.CharField(max_length=20, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    record_name = models.CharField(max_length=20, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    model = models.CharField(max_length=20, blank=True, null=True)
    use_active_domain = models.BooleanField(blank=True, null=True)
    email_from = models.CharField(max_length=20, blank=True, null=True)
    reply_to = models.CharField(max_length=20, blank=True, null=True)
    author = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    message_type = models.CharField(max_length=20)
    template = models.ForeignKey('MailTemplate', models.DO_NOTHING, blank=True, null=True)
    mass_mailing_campaign = models.ForeignKey('MailMassMailingCampaign', models.DO_NOTHING, blank=True, null=True)
    mass_mailing = models.ForeignKey('MailMassMailing', models.DO_NOTHING, blank=True, null=True)
    mass_mailing_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_compose_message'


class MailComposeMessageIrAttachmentsRel(models.Model):
    wizard = models.ForeignKey(MailComposeMessage, models.DO_NOTHING)
    attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_compose_message_ir_attachments_rel'
        unique_together = (('wizard', 'attachment'),)


class MailComposeMessageMailMassMailingListRel(models.Model):
    mail_compose_message = models.ForeignKey(MailComposeMessage, models.DO_NOTHING)
    mail_mass_mailing_list = models.ForeignKey('MailMassMailingList', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_compose_message_mail_mass_mailing_list_rel'
        unique_together = (('mail_compose_message', 'mail_mass_mailing_list'),)


class MailComposeMessageResPartnerRel(models.Model):
    wizard = models.ForeignKey(MailComposeMessage, models.DO_NOTHING)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_compose_message_res_partner_rel'
        unique_together = (('wizard', 'partner'),)


class MailFollowers(models.Model):
    res_model = models.CharField(max_length=20)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    channel = models.ForeignKey(MailChannel, models.DO_NOTHING, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_followers'
        unique_together = (('res_model', 'res_id', 'channel'), ('res_model', 'res_id', 'partner'),)


class MailFollowersMailMessageSubtypeRel(models.Model):
    mail_followers = models.ForeignKey(MailFollowers, models.DO_NOTHING)
    mail_message_subtype = models.ForeignKey('MailMessageSubtype', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_followers_mail_message_subtype_rel'
        unique_together = (('mail_followers', 'mail_message_subtype'),)


class MailMail(models.Model):
    mail_message = models.ForeignKey('MailMessage', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    notification = models.BooleanField(blank=True, null=True)
    auto_delete = models.BooleanField(blank=True, null=True)
    body_html = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    email_to = models.TextField(blank=True, null=True)
    headers = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    references = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    email_cc = models.CharField(max_length=20, blank=True, null=True)
    failure_reason = models.TextField(blank=True, null=True)
    fetchmail_server = models.ForeignKey(FetchmailServer, models.DO_NOTHING, blank=True, null=True)
    mailing = models.ForeignKey('MailMassMailing', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_mail'


class MailMailResPartnerRel(models.Model):
    mail_mail = models.ForeignKey(MailMail, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_mail_res_partner_rel'
        unique_together = (('mail_mail', 'res_partner'),)


class MailMailStatistics(models.Model):
    replied = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    state_update = models.DateTimeField(blank=True, null=True)
    mail_mail = models.ForeignKey(MailMail, models.DO_NOTHING, blank=True, null=True)
    mass_mailing_campaign = models.ForeignKey('MailMassMailingCampaign', models.DO_NOTHING, blank=True, null=True)
    mass_mailing = models.ForeignKey('MailMassMailing', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    opened = models.DateTimeField(blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    message_id = models.CharField(max_length=20, blank=True, null=True)
    sent = models.DateTimeField(blank=True, null=True)
    scheduled = models.DateTimeField(blank=True, null=True)
    mail_mail_id_int = models.IntegerField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    exception = models.DateTimeField(blank=True, null=True)
    model = models.CharField(max_length=20, blank=True, null=True)
    bounced = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_mail_statistics'


class MailMassMailing(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    campaign = models.ForeignKey('UtmCampaign', models.DO_NOTHING, blank=True, null=True)
    mass_mailing_campaign = models.ForeignKey('MailMassMailingCampaign', models.DO_NOTHING, blank=True, null=True)
    schedule_date = models.DateTimeField(blank=True, null=True)
    contact_ab_pc = models.IntegerField(blank=True, null=True)
    mailing_model = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    mailing_domain = models.CharField(max_length=20, blank=True, null=True)
    keep_archives = models.BooleanField(blank=True, null=True)
    sent_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    body_html = models.TextField(blank=True, null=True)
    reply_to = models.CharField(max_length=20, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    name = models.CharField(max_length=20)
    medium = models.ForeignKey('UtmMedium', models.DO_NOTHING, blank=True, null=True)
    reply_to_mode = models.CharField(max_length=20)
    source = models.ForeignKey('UtmSource', models.DO_NOTHING, blank=True, null=True)
    email_from = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'mail_mass_mailing'


class MailMassMailingCampaign(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    campaign = models.ForeignKey('UtmCampaign', models.DO_NOTHING)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    unique_ab_testing = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    stage = models.ForeignKey('MailMassMailingStage', models.DO_NOTHING)
    name = models.CharField(max_length=20)
    medium = models.ForeignKey('UtmMedium', models.DO_NOTHING, blank=True, null=True)
    source = models.ForeignKey('UtmSource', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_mass_mailing_campaign'


class MailMassMailingContact(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    opt_out = models.BooleanField(blank=True, null=True)
    unsubscription_date = models.DateTimeField(blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    email = models.CharField(max_length=20)
    write_date = models.DateTimeField(blank=True, null=True)
    list = models.ForeignKey('MailMassMailingList', models.DO_NOTHING)
    message_bounce = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_mass_mailing_contact'


class MailMassMailingList(models.Model):
    popup_redirect_url = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    popup_content = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_mass_mailing_list'


class MailMassMailingListRel(models.Model):
    mail_mass_mailing = models.ForeignKey(MailMassMailing, models.DO_NOTHING)
    mail_mass_mailing_list = models.ForeignKey(MailMassMailingList, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_mass_mailing_list_rel'
        unique_together = (('mail_mass_mailing', 'mail_mass_mailing_list'),)


class MailMassMailingStage(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    sequence = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_mass_mailing_stage'


class MailMassMailingTag(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=20)
    color = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_mass_mailing_tag'


class MailMassMailingTagRel(models.Model):
    tag = models.ForeignKey(MailMassMailingCampaign, models.DO_NOTHING)
    campaign = models.ForeignKey(MailMassMailingTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_mass_mailing_tag_rel'
        unique_together = (('tag', 'campaign'),)


class MailMassMailingTest(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    email_to = models.CharField(max_length=20)
    write_date = models.DateTimeField(blank=True, null=True)
    mass_mailing = models.ForeignKey(MailMassMailing, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_mass_mailing_test'


class MailMessage(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    mail_server = models.ForeignKey(IrMailServer, models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    subject = models.CharField(max_length=20, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    subtype = models.ForeignKey('MailMessageSubtype', models.DO_NOTHING, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    message_id = models.CharField(max_length=20, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    record_name = models.CharField(max_length=20, blank=True, null=True)
    no_auto_thread = models.BooleanField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    model = models.CharField(max_length=20, blank=True, null=True)
    reply_to = models.CharField(max_length=20, blank=True, null=True)
    author = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    message_type = models.CharField(max_length=20)
    email_from = models.CharField(max_length=20, blank=True, null=True)
    website_published = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_message'


class MailMessageMailChannelRel(models.Model):
    mail_message = models.ForeignKey(MailMessage, models.DO_NOTHING)
    mail_channel = models.ForeignKey(MailChannel, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_message_mail_channel_rel'
        unique_together = (('mail_message', 'mail_channel'),)


class MailMessageResPartnerNeedactionRel(models.Model):
    mail_message = models.ForeignKey(MailMessage, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_message_res_partner_needaction_rel'
        unique_together = (('mail_message', 'res_partner'),)


class MailMessageResPartnerRel(models.Model):
    mail_message = models.ForeignKey(MailMessage, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_message_res_partner_rel'
        unique_together = (('mail_message', 'res_partner'),)


class MailMessageResPartnerStarredRel(models.Model):
    mail_message = models.ForeignKey(MailMessage, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_message_res_partner_starred_rel'
        unique_together = (('mail_message', 'res_partner'),)


class MailMessageSubtype(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    default = models.BooleanField(blank=True, null=True)
    res_model = models.CharField(max_length=20, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    internal = models.BooleanField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    relation_field = models.CharField(max_length=20, blank=True, null=True)
    hidden = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'mail_message_subtype'


class MailShortcode(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=20, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    source = models.CharField(max_length=20)
    shortcode_type = models.CharField(max_length=20)
    substitution = models.CharField(max_length=20)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_shortcode'


class MailTemplate(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    auto_delete = models.BooleanField(blank=True, null=True)
    mail_server = models.ForeignKey(IrMailServer, models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    partner_to = models.CharField(max_length=20, blank=True, null=True)
    ref_ir_act_window = models.ForeignKey(IrActWindow, models.DO_NOTHING, db_column='ref_ir_act_window', blank=True, null=True)
    subject = models.CharField(max_length=20, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    report_template = models.ForeignKey(IrActReportXml, models.DO_NOTHING, db_column='report_template', blank=True, null=True)
    ref_ir_value = models.ForeignKey(IrValues, models.DO_NOTHING, db_column='ref_ir_value', blank=True, null=True)
    user_signature = models.BooleanField(blank=True, null=True)
    null_value = models.CharField(max_length=20, blank=True, null=True)
    email_cc = models.CharField(max_length=20, blank=True, null=True)
    model = models.ForeignKey(IrModel, models.DO_NOTHING, blank=True, null=True, related_name='model%(app_label)s_%(class)s_related')
    sub_model_object_field = models.ForeignKey(IrModelFields, models.DO_NOTHING, db_column='sub_model_object_field', blank=True, null=True, related_name='sub_model_object_field%(app_label)s_%(class)s_related')
    body_html = models.TextField(blank=True, null=True)
    email_to = models.CharField(max_length=20, blank=True, null=True)
    sub_object = models.ForeignKey(IrModel, models.DO_NOTHING, db_column='sub_object', blank=True, null=True, related_name='sub_object%(app_label)s_%(class)s_related')
    copyvalue = models.CharField(max_length=20, blank=True, null=True)
    lang = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    model_object_field = models.ForeignKey(IrModelFields, models.DO_NOTHING, db_column='model_object_field', blank=True, null=True)
    report_name = models.CharField(max_length=20, blank=True, null=True)
    use_default_to = models.BooleanField(blank=True, null=True)
    reply_to = models.CharField(max_length=20, blank=True, null=True)
    model_0 = models.CharField(db_column='model', max_length=20, blank=True, null=True)  # Field renamed because of name conflict.
    email_from = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_template'


class MailTrackingValue(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    field_type = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    old_value_datetime = models.DateTimeField(blank=True, null=True)
    old_value_monetary = models.FloatField(blank=True, null=True)
    new_value_monetary = models.FloatField(blank=True, null=True)
    mail_message = models.ForeignKey(MailMessage, models.DO_NOTHING)
    old_value_char = models.CharField(max_length=20, blank=True, null=True)
    old_value_float = models.FloatField(blank=True, null=True)
    new_value_text = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    new_value_float = models.FloatField(blank=True, null=True)
    field = models.CharField(max_length=20)
    old_value_text = models.TextField(blank=True, null=True)
    field_desc = models.CharField(max_length=20)
    new_value_char = models.CharField(max_length=20, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    new_value_datetime = models.DateTimeField(blank=True, null=True)
    new_value_integer = models.IntegerField(blank=True, null=True)
    old_value_integer = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_tracking_value'


class MailWizardInvite(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    res_model = models.CharField(max_length=20)
    send_mail = models.BooleanField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_wizard_invite'


class MailWizardInviteResPartnerRel(models.Model):
    mail_wizard_invite = models.ForeignKey(MailWizardInvite, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_wizard_invite_res_partner_rel'
        unique_together = (('mail_wizard_invite', 'res_partner'),)


class MakeProcurement(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING)
    date_planned = models.DateField()
    res_model = models.CharField(max_length=20, blank=True, null=True)
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING)
    uom = models.ForeignKey('ProductUom', models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    qty = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'make_procurement'


class MakeProcurementStockLocationRouteRel(models.Model):
    make_procurement = models.ForeignKey(MakeProcurement, models.DO_NOTHING)
    stock_location_route = models.ForeignKey('StockLocationRoute', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'make_procurement_stock_location_route_rel'
        unique_together = (('make_procurement', 'stock_location_route'),)


class MarketingConfigSettings(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    module_marketing_campaign = models.BooleanField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marketing_config_settings'


class MassMailingConfigSettings(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    group_website_popup_on_exit = models.IntegerField(blank=True, null=True)
    module_mass_mailing_themes = models.BooleanField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    group_mass_mailing_campaign = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mass_mailing_config_settings'


class MassMailingIrAttachmentsRel(models.Model):
    mass_mailing = models.ForeignKey(MailMassMailing, models.DO_NOTHING)
    attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mass_mailing_ir_attachments_rel'
        unique_together = (('mass_mailing', 'attachment'),)


class MeetingCategoryRel(models.Model):
    event = models.ForeignKey(CalendarEvent, models.DO_NOTHING)
    type = models.ForeignKey(CalendarEventType, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'meeting_category_rel'
        unique_together = (('event', 'type'),)


class MergeOpportunityRel(models.Model):
    merge = models.ForeignKey(CrmMergeOpportunity, models.DO_NOTHING)
    opportunity = models.ForeignKey(CrmLead, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'merge_opportunity_rel'
        unique_together = (('merge', 'opportunity'),)


class MessageAttachmentRel(models.Model):
    message = models.ForeignKey(MailMessage, models.DO_NOTHING)
    attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'message_attachment_rel'
        unique_together = (('message', 'attachment'),)


class PartnerUpdateFromPadronRel(models.Model):
    update = models.ForeignKey('ResPartnerUpdateFromPadronWizard', models.DO_NOTHING)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'partner_update_from_padron_rel'
        unique_together = (('update', 'partner'),)


class PaymentAcquirer(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    fees_active = models.BooleanField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    cancel_msg = models.TextField(blank=True, null=True)
    registration_view_template = models.ForeignKey(IrUiView, models.DO_NOTHING, blank=True, null=True)
    fees_dom_fixed = models.FloatField(blank=True, null=True)
    fees_int_fixed = models.FloatField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    sequence = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    environment = models.CharField(max_length=20, blank=True, null=True)
    provider = models.CharField(max_length=20)
    website_published = models.BooleanField(blank=True, null=True)
    auto_confirm = models.CharField(max_length=20)
    pending_msg = models.TextField(blank=True, null=True)
    post_msg = models.TextField(blank=True, null=True)
    fees_int_var = models.FloatField(blank=True, null=True)
    done_msg = models.TextField(blank=True, null=True)
    pre_msg = models.TextField(blank=True, null=True)
    error_msg = models.TextField(blank=True, null=True)
    fees_dom_var = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=20)
    view_template = models.ForeignKey(IrUiView, models.DO_NOTHING, related_name='view_template%(app_label)s_%(class)s_related')
    todopago_secret_key = models.CharField(max_length=20, blank=True, null=True)
    todopago_client_id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_acquirer'


class PaymentMethod(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    acquirer_ref = models.CharField(max_length=20)
    acquirer = models.ForeignKey(PaymentAcquirer, models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'payment_method'


class PaymentTransaction(models.Model):
    state_message = models.TextField(blank=True, null=True)
    callback_eval = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    reference = models.CharField(max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    acquirer = models.ForeignKey(PaymentAcquirer, models.DO_NOTHING)
    fees = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    payment_method = models.ForeignKey(PaymentMethod, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    partner_name = models.CharField(max_length=20, blank=True, null=True)
    partner_phone = models.CharField(max_length=10, blank=True, null=True)
    state = models.CharField(max_length=10)
    type = models.CharField(max_length=5)
    partner_country = models.ForeignKey('ResCountry', models.DO_NOTHING)
    acquirer_reference = models.CharField(max_length=10, blank=True, null=True)
    partner_address = models.CharField(max_length=30, blank=True, null=True)
    partner_email = models.CharField(max_length=30, blank=True, null=True)
    partner_lang = models.CharField(max_length=20, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    partner_zip = models.CharField(max_length=5, blank=True, null=True)
    html_3ds = models.CharField(max_length=20, blank=True, null=True)
    date_validate = models.DateTimeField(blank=True, null=True)
    partner_city = models.CharField(max_length=5, blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    sale_order = models.ForeignKey('SaleOrder', models.DO_NOTHING, blank=True, null=True)
    todopago_return_url = models.CharField(db_column='todopago_Return_url', max_length=20, blank=True, null=True)  # Field name made lowercase.
    todopago_publicrequestkey = models.CharField(db_column='todopago_PublicRequestKey', max_length=20, blank=True, null=True)  # Field name made lowercase.
    todopago_answer = models.CharField(db_column='todopago_Answer', max_length=20, blank=True, null=True)  # Field name made lowercase.
    todopago_requestkey = models.CharField(db_column='todopago_RequestKey', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'payment_transaction'


class PortalWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    welcome_message = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    portal = models.ForeignKey('ResGroups', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'portal_wizard'


class PortalWizardUser(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    wizard = models.ForeignKey(PortalWizard, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    email = models.CharField(max_length=240, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    in_portal = models.BooleanField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'portal_wizard_user'


class PrintPrenumberedChecks(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    next_check_number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'print_prenumbered_checks'


class ProcurementGroup(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    move_type = models.CharField(max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procurement_group'


class ProcurementOrder(models.Model):
    origin = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING)
    product_uom = models.ForeignKey('ProductUom', models.DO_NOTHING, db_column='product_uom')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    date_planned = models.DateTimeField()
    message_last_post = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    priority = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    write_date = models.DateTimeField(blank=True, null=True)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    rule = models.ForeignKey('ProcurementRule', models.DO_NOTHING, blank=True, null=True)
    group = models.ForeignKey(ProcurementGroup, models.DO_NOTHING, blank=True, null=True)
    name = models.TextField()
    sale_line = models.ForeignKey('SaleOrderLine', models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey('StockLocation', models.DO_NOTHING, blank=True, null=True)
    partner_dest = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    orderpoint = models.ForeignKey('StockWarehouseOrderpoint', models.DO_NOTHING, blank=True, null=True)
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    move_dest = models.ForeignKey('StockMove', models.DO_NOTHING, blank=True, null=True)
    purchase_line = models.ForeignKey('PurchaseOrderLine', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procurement_order'


class ProcurementOrderComputeAll(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'procurement_order_compute_all'


class ProcurementOrderpointCompute(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'procurement_orderpoint_compute'


class ProcurementRule(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    sequence = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    action = models.CharField(max_length=20)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    group = models.ForeignKey(ProcurementGroup, models.DO_NOTHING, blank=True, null=True)
    group_propagation_option = models.CharField(max_length=20, blank=True, null=True)
    partner_address = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey('StockLocation', models.DO_NOTHING, blank=True, null=True, related_name='location%(app_label)s_%(class)s_related')
    location_src = models.ForeignKey('StockLocation', models.DO_NOTHING, blank=True, null=True)
    picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING, blank=True, null=True)
    delay = models.IntegerField(blank=True, null=True)
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True, related_name='warehouse%(app_label)s_%(class)s_related')
    propagate = models.BooleanField(blank=True, null=True)
    procure_method = models.CharField(max_length=20)
    route_sequence = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    route = models.ForeignKey('StockLocationRoute', models.DO_NOTHING, blank=True, null=True)
    propagate_warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procurement_rule'


class ProductAccessoryRel(models.Model):
    src = models.ForeignKey('ProductTemplate', models.DO_NOTHING)
    dest = models.ForeignKey('ProductProduct', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_accessory_rel'
        unique_together = (('src', 'dest'),)


class ProductAlternativeRel(models.Model):
    src = models.ForeignKey('ProductTemplate', models.DO_NOTHING, related_name='src%(app_label)s_%(class)s_related')
    dest = models.ForeignKey('ProductTemplate', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_alternative_rel'
        unique_together = (('src', 'dest'),)


class ProductAttribute(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    sequence = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_attribute'


class ProductAttributeLine(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING)
    attribute = models.ForeignKey(ProductAttribute, models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_attribute_line'


class ProductAttributeLineProductAttributeValueRel(models.Model):
    line = models.ForeignKey(ProductAttributeLine, models.DO_NOTHING)
    val = models.ForeignKey('ProductAttributeValue', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_attribute_line_product_attribute_value_rel'
        unique_together = (('line', 'val'),)


class ProductAttributePrice(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    price_extra = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING)
    value = models.ForeignKey('ProductAttributeValue', models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'product_attribute_price'


class ProductAttributeValue(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    sequence = models.IntegerField(blank=True, null=True)
    attribute = models.ForeignKey(ProductAttribute, models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    color = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_attribute_value'
        unique_together = (('name', 'attribute'),)


class ProductAttributeValueProductProductRel(models.Model):
    att = models.ForeignKey(ProductAttributeValue, models.DO_NOTHING)
    prod = models.ForeignKey('ProductProduct', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_attribute_value_product_product_rel'
        unique_together = (('att', 'prod'),)


class ProductCatalog(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    taxes_included = models.BooleanField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    use_planned_price = models.BooleanField(blank=True, null=True)
    product_catalog_report = models.ForeignKey('ProductProductCatalogReport', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_catalog'


class ProductCatalogReportCategories(models.Model):
    product_catalog_report = models.ForeignKey('ProductProductCatalogReport', models.DO_NOTHING)
    category = models.ForeignKey('ProductCategory', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_catalog_report_categories'
        unique_together = (('product_catalog_report', 'category'),)


class ProductCatalogReportCategoriesPublic(models.Model):
    product_catalog_report = models.ForeignKey('ProductProductCatalogReport', models.DO_NOTHING)
    category = models.ForeignKey('ProductPublicCategory', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_catalog_report_categories_public'
        unique_together = (('product_catalog_report', 'category'),)


class ProductCatalogReportPricelists(models.Model):
    product_catalog_report = models.ForeignKey('ProductProductCatalogReport', models.DO_NOTHING)
    pricelist = models.ForeignKey('Product_price_list', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_catalog_report_pricelists'
        unique_together = (('product_catalog_report', 'pricelist'),)


class ProductCategory(models.Model):
    parent_left = models.IntegerField(blank=True, null=True)
    parent_right = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    sequence = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    removal_strategy = models.ForeignKey('ProductRemoval', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_category'


class ProductPackaging(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    sequence = models.IntegerField(blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'product_packaging'


class ProductPriceHistory(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    datetime = models.DateTimeField(blank=True, null=True)
    cost = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'product_price_history'


class Product_price_list(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    price_list = models.ForeignKey('Product_price_list', models.DO_NOTHING, db_column='price_list')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    qty1 = models.IntegerField(blank=True, null=True)
    qty2 = models.IntegerField(blank=True, null=True)
    qty3 = models.IntegerField(blank=True, null=True)
    qty4 = models.IntegerField(blank=True, null=True)
    qty5 = models.IntegerField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_price_list'


class Product_Pricelist(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_pricelist'


class ProductPricelistItem(models.Model):
    fixed_price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    price_discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sequence = models.IntegerField()
    price_max_margin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    applied_on = models.CharField(max_length=20)
    min_quantity = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    percent_price = models.FloatField(blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING, blank=True, null=True)
    pricelist = models.ForeignKey(Product_price_list, models.DO_NOTHING, blank=True, null=True, related_name='pricelist%(app_label)s_%(class)s_related')
    price_min_margin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    compute_price = models.CharField(max_length=20, blank=True, null=True)
    base = models.CharField(max_length=20)
    write_date = models.DateTimeField(blank=True, null=True)
    categ = models.ForeignKey(ProductCategory, models.DO_NOTHING, blank=True, null=True)
    price_surcharge = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_round = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True)
    base_pricelist = models.ForeignKey(Product_price_list, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_pricelist_item'


class ProductProduct(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    default_code = models.CharField(max_length=20, blank=True, null=True)
    name_template = models.CharField(max_length=20, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    message_last_post = models.DateTimeField(blank=True, null=True)
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING, related_name='product_tmpl%(app_label)s_%(class)s_related')
    barcode = models.CharField(unique=True, max_length=20, blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'product_product'


class ProductProductCatalogReport(models.Model):
    product_type = models.CharField(max_length=20)
    only_with_stock = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=20)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    report_xml = models.ForeignKey(IrActReportXml, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    include_sub_categories = models.BooleanField(blank=True, null=True)
    prod_display_type = models.CharField(max_length=20, blank=True, null=True)
    print_product_uom = models.BooleanField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    categories_order = models.CharField(max_length=20, blank=True, null=True)
    taxes_included = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    products_order = models.CharField(max_length=20, blank=True, null=True)
    category_type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'product_product_catalog_report'


class ProductPublicCategory(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    sequence = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    website_meta_description = models.TextField(blank=True, null=True)
    website_meta_title = models.CharField(max_length=20, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    website_meta_keywords = models.CharField(max_length=20, blank=True, null=True)
    parent_left = models.IntegerField(blank=True, null=True)
    parent_right = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_public_category'


class ProductPublicCategoryProductTemplateRel(models.Model):
    product_template = models.ForeignKey('ProductTemplate', models.DO_NOTHING)
    product_public_category = models.ForeignKey(ProductPublicCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_public_category_product_template_rel'
        unique_together = (('product_template', 'product_public_category'),)


class ProductPutaway(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    method = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'product_putaway'


class ProductRemoval(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    method = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'product_removal'


class ProductStyle(models.Model):
    html_class = models.CharField(max_length=20, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_style'


class ProductStyleProductTemplateRel(models.Model):
    product_template = models.ForeignKey('ProductTemplate', models.DO_NOTHING)
    product_style = models.ForeignKey(ProductStyle, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_style_product_template_rel'
        unique_together = (('product_template', 'product_style'),)


class ProductSupplierTaxesRel(models.Model):
    prod = models.ForeignKey('ProductTemplate', models.DO_NOTHING)
    tax = models.ForeignKey(AccountTax, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_supplier_taxes_rel'
        unique_together = (('prod', 'tax'),)


class ProductSupplierinfo(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    product_name = models.CharField(max_length=20, blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    delay = models.IntegerField()
    write_date = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(max_digits=65535, decimal_places=65535)
    min_qty = models.FloatField()
    product_code = models.CharField(max_length=20, blank=True, null=True)
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING, blank=True, null=True)
    name = models.ForeignKey('ResPartner', models.DO_NOTHING, db_column='name')

    class Meta:
        managed = False
        db_table = 'product_supplierinfo'


class ProductTaxesRel(models.Model):
    prod = models.ForeignKey('ProductTemplate', models.DO_NOTHING)
    tax = models.ForeignKey(AccountTax, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_taxes_rel'
        unique_together = (('prod', 'tax'),)


class ProductTemplate(models.Model):
    warranty = models.FloatField(blank=True, null=True)
    list_price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    uom = models.ForeignKey('ProductUom', models.DO_NOTHING, related_name='uom%(app_label)s_%(class)s_related')
    description_purchase = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    sale_ok = models.BooleanField(blank=True, null=True)
    categ = models.ForeignKey(ProductCategory, models.DO_NOTHING)
    product_manager = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='product_manager', blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    uom_po = models.ForeignKey('ProductUom', models.DO_NOTHING)
    description_sale = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    volume = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    rental = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    track_service = models.CharField(max_length=20, blank=True, null=True)
    invoice_policy = models.CharField(max_length=20, blank=True, null=True)
    description_picking = models.TextField(blank=True, null=True)
    sale_delay = models.FloatField(blank=True, null=True)
    tracking = models.CharField(max_length=20)
    purchase_ok = models.BooleanField(blank=True, null=True)
    purchase_method = models.CharField(max_length=20, blank=True, null=True)
    website_description = models.TextField(blank=True, null=True)
    website_sequence = models.IntegerField(blank=True, null=True)
    website_meta_description = models.TextField(blank=True, null=True)
    website_meta_keywords = models.CharField(max_length=20, blank=True, null=True)
    website_meta_title = models.CharField(max_length=20, blank=True, null=True)
    website_published = models.BooleanField(blank=True, null=True)
    website_size_x = models.IntegerField(blank=True, null=True)
    website_size_y = models.IntegerField(blank=True, null=True)
    force_currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_template'


class ProductUom(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    rounding = models.DecimalField(max_digits=65535, decimal_places=65535)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    active = models.BooleanField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    factor = models.DecimalField(max_digits=65535, decimal_places=65535)
    uom_type = models.CharField(max_length=5)
    category = models.ForeignKey('ProductUomCateg', models.DO_NOTHING)
    afip_code = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_uom'


class ProductUomCateg(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_uom_categ'


class ProjectConfigSettings(models.Model):
    module_sale_service = models.IntegerField(blank=True, null=True)
    module_pad = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    module_project_timesheet_synchro = models.BooleanField(blank=True, null=True)
    module_project_forecast = models.BooleanField(blank=True, null=True)
    module_project_issue_sheet = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    module_rating_project = models.IntegerField(blank=True, null=True)
    generate_project_alias = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    group_time_work_estimation_tasks = models.IntegerField(blank=True, null=True)
    module_project_timesheet = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_config_settings'


class ProjectProject(models.Model):
    alias_model = models.CharField(max_length=20)
    create_date = models.DateTimeField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    alias = models.ForeignKey(MailAlias, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    privacy_visibility = models.CharField(max_length=20)
    label_tasks = models.CharField(max_length=20, blank=True, null=True)
    analytic_account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    state = models.CharField(max_length=20)
    sequence = models.IntegerField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    resource_calendar = models.ForeignKey('ResourceCalendar', models.DO_NOTHING, blank=True, null=True)
    percentage_satisfaction_project = models.IntegerField(blank=True, null=True)
    is_visible_happy_customer = models.BooleanField(blank=True, null=True)
    percentage_satisfaction_task = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_project'


class ProjectTags(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=20)
    color = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_tags'


class ProjectTagsProjectTaskRel(models.Model):
    project_task = models.ForeignKey('ProjectTask', models.DO_NOTHING)
    project_tags = models.ForeignKey(ProjectTags, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'project_tags_project_task_rel'
        unique_together = (('project_task', 'project_tags'),)


class ProjectTask(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    planned_hours = models.FloatField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    displayed_image = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    date_start = models.DateTimeField(blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    priority = models.CharField(max_length=20, blank=True, null=True)
    project = models.ForeignKey(ProjectProject, models.DO_NOTHING, blank=True, null=True)
    date_last_stage_update = models.DateTimeField(blank=True, null=True)
    date_assign = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    kanban_state = models.CharField(max_length=20)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    stage = models.ForeignKey('ProjectTaskType', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=128)
    date_deadline = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    remaining_hours = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_task'


class ProjectTaskHistory(models.Model):
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    task = models.ForeignKey(ProjectTask, models.DO_NOTHING)
    type = models.ForeignKey('ProjectTaskType', models.DO_NOTHING, blank=True, null=True)
    kanban_state = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    planned_hours = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    remaining_hours = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_task_history'


class ProjectTaskParentRel(models.Model):
    parent = models.ForeignKey(ProjectTask, models.DO_NOTHING, related_name='parent%(app_label)s_%(class)s_related')
    task = models.ForeignKey(ProjectTask, models.DO_NOTHING, related_name='task%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'project_task_parent_rel'
        unique_together = (('parent', 'task'),)


class ProjectTaskType(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    legend_done = models.CharField(max_length=20, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    fold = models.BooleanField(blank=True, null=True)
    legend_blocked = models.CharField(max_length=20, blank=True, null=True)
    legend_priority = models.CharField(max_length=20, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    legend_normal = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=20)
    rating_template = models.ForeignKey(MailTemplate, models.DO_NOTHING, blank=True, null=True)
    auto_validation_kanban_state = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_task_type'


class ProjectTaskTypeRel(models.Model):
    type = models.ForeignKey(ProjectTaskType, models.DO_NOTHING)
    project = models.ForeignKey(ProjectProject, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'project_task_type_rel'
        unique_together = (('type', 'project'),)


class PurchaseConfigSettings(models.Model):
    group_uom = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    module_stock_dropshipping = models.IntegerField(blank=True, null=True)
    group_costing_method = models.IntegerField(blank=True, null=True)
    group_advance_purchase_requisition = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    group_manage_vendor_price = models.IntegerField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    group_product_variant = models.IntegerField(blank=True, null=True)
    module_purchase_requisition = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase_config_settings'


class PurchaseOrder(models.Model):
    origin = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    date_order = models.DateTimeField()
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name='partner%(app_label)s_%(class)s_related')
    dest_address = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    amount_untaxed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING)
    message_last_post = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    amount_tax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    fiscal_position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING, blank=True, null=True)
    incoterm = models.ForeignKey('StockIncoterms', models.DO_NOTHING, blank=True, null=True)
    payment_term = models.ForeignKey(AccountPaymentTerm, models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    partner_ref = models.CharField(max_length=20, blank=True, null=True)
    date_approve = models.DateField(blank=True, null=True)
    amount_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    invoice_status = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=20)
    notes = models.TextField(blank=True, null=True)
    group = models.ForeignKey(ProcurementGroup, models.DO_NOTHING, blank=True, null=True)
    internal_notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase_order'


class PurchaseOrderLine(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    product_uom = models.ForeignKey(ProductUom, models.DO_NOTHING, db_column='product_uom')
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535)
    price_subtotal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    qty_received = models.FloatField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    price_tax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    account_analytic = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey(PurchaseOrder, models.DO_NOTHING)
    qty_invoiced = models.FloatField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    name = models.TextField()
    price_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    date_planned = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'purchase_order_line'


class RatingRating(models.Model):
    rating = models.FloatField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True, related_name='partner%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    access_token = models.CharField(max_length=20, blank=True, null=True)
    res_model = models.CharField(max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    res_name = models.CharField(max_length=20, blank=True, null=True)
    message = models.ForeignKey(MailMessage, models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    rated_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    res_id = models.IntegerField()
    website_published = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rating_rating'


class RelModulesLangexport(models.Model):
    wiz = models.ForeignKey(BaseLanguageExport, models.DO_NOTHING)
    module = models.ForeignKey(IrModuleModule, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rel_modules_langexport'
        unique_together = (('wiz', 'module'),)


class RelServerActions(models.Model):
    server = models.ForeignKey(IrActServer, models.DO_NOTHING, related_name='server%(app_label)s_%(class)s_related')
    action = models.ForeignKey(IrActServer, models.DO_NOTHING, related_name='action%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'rel_server_actions'
        unique_together = (('server', 'action'),)


class Report(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'report'


class ReportAccountDocumentTypeRel(models.Model):
    report = models.ForeignKey(IrActReportXml, models.DO_NOTHING)
    document_type = models.ForeignKey(AccountDocumentType, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'report_account_document_type_rel'
        unique_together = (('report', 'document_type'),)


class ReportAccountJournalRel(models.Model):
    report = models.ForeignKey(IrActReportXml, models.DO_NOTHING)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'report_account_journal_rel'
        unique_together = (('report', 'journal'),)


class ReportAerooInstaller(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    link = models.CharField(max_length=128, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_aeroo_installer'


class ReportConfigurationDefault(models.Model):
    value_text = models.TextField(blank=True, null=True)
    value_boolean = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=256)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    override_values = models.BooleanField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    value_type = models.CharField(max_length=20)
    write_date = models.DateTimeField(blank=True, null=True)
    apply_to_all = models.BooleanField(blank=True, null=True)
    apply_to_model = models.ForeignKey(IrModel, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_configuration_default'


class ReportConfigurationLine(models.Model):
    value_text = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=256)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    value_type = models.CharField(max_length=20)
    write_date = models.DateTimeField(blank=True, null=True)
    value_boolean = models.BooleanField(blank=True, null=True)
    report = models.ForeignKey(IrActReportXml, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'report_configuration_line'


class ReportConfigurationReceiptbookRelation(models.Model):
    report_configuration = models.ForeignKey(IrActReportXml, models.DO_NOTHING)
    receiptbook = models.ForeignKey(AccountPaymentReceiptbook, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'report_configuration_receiptbook_relation'
        unique_together = (('report_configuration', 'receiptbook'),)


class ReportConfigurationStockBookRel(models.Model):
    report_configuration = models.ForeignKey(IrActReportXml, models.DO_NOTHING)
    book = models.ForeignKey('StockBook', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'report_configuration_stock_book_rel'
        unique_together = (('report_configuration', 'book'),)


class ReportConfigurationStockPickingTypeRel(models.Model):
    report_configuration = models.ForeignKey(IrActReportXml, models.DO_NOTHING)
    picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'report_configuration_stock_picking_type_rel'
        unique_together = (('report_configuration', 'picking_type'),)


class ReportMimetypes(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    code = models.CharField(max_length=16)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=64)
    compatible_types = models.CharField(max_length=128, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    filter_name = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_mimetypes'


class ReportPaperformat(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    page_width = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    format = models.CharField(max_length=5, blank=True, null=True)
    default = models.BooleanField(blank=True, null=True)
    header_line = models.BooleanField(blank=True, null=True)
    header_spacing = models.IntegerField(blank=True, null=True)
    dpi = models.IntegerField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    margin_right = models.FloatField(blank=True, null=True)
    margin_top = models.FloatField(blank=True, null=True)
    margin_left = models.FloatField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    margin_bottom = models.FloatField(blank=True, null=True)
    page_height = models.IntegerField(blank=True, null=True)
    orientation = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_paperformat'


class ReportStylesheets(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=64)
    report_styles = models.BinaryField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_stylesheets'


class ResBank(models.Model):
    city = models.CharField(max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    zip = models.CharField(max_length=20, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, db_column='country', blank=True, null=True)
    street2 = models.CharField(max_length=20, blank=True, null=True)
    bic = models.CharField(max_length=20, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    email = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    state = models.ForeignKey('ResCountryState', models.DO_NOTHING, db_column='state', blank=True, null=True)
    street = models.CharField(max_length=20, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_bank'


class ResCompany(models.Model):
    name = models.CharField(unique=True, max_length=20)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    rml_footer = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    rml_header = models.TextField()
    rml_paper_format = models.CharField(max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    logo_web = models.BinaryField(blank=True, null=True)
    font = models.ForeignKey('ResFont', models.DO_NOTHING, db_column='font', blank=True, null=True)
    account_no = models.CharField(max_length=5, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    custom_footer = models.BooleanField(blank=True, null=True)
    phone = models.CharField(max_length=64, blank=True, null=True)
    rml_header2 = models.TextField()
    rml_header3 = models.TextField()
    write_date = models.DateTimeField(blank=True, null=True)
    rml_header1 = models.CharField(max_length=5, blank=True, null=True)
    company_registry = models.CharField(max_length=64, blank=True, null=True)
    paperformat = models.ForeignKey(ReportPaperformat, models.DO_NOTHING, blank=True, null=True)
    fiscalyear_lock_date = models.DateField(blank=True, null=True)
    bank_account_code_prefix = models.CharField(max_length=20, blank=True, null=True)
    cash_account_code_prefix = models.CharField(max_length=20, blank=True, null=True)
    anglo_saxon_accounting = models.BooleanField(blank=True, null=True)
    fiscalyear_last_day = models.IntegerField()
    property_stock_account_input_categ = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True, related_name='property_stock_account_input_categ%(app_label)s_%(class)s_related')
    property_stock_valuation_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True, related_name='property_stock_valuation_account%(app_label)s_%(class)s_related')
    expects_chart_of_accounts = models.BooleanField(blank=True, null=True)
    transfer_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True, related_name='transfer_account%(app_label)s_%(class)s_related')
    property_stock_account_output_categ = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True, related_name='property_stock_account_output_categ%(app_label)s_%(class)s_related')
    currency_exchange_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True)
    period_lock_date = models.DateField(blank=True, null=True)
    paypal_account = models.CharField(max_length=128, blank=True, null=True)
    accounts_code_digits = models.IntegerField(blank=True, null=True)
    chart_template = models.ForeignKey(AccountChartTemplate, models.DO_NOTHING, blank=True, null=True)
    overdue_msg = models.TextField(blank=True, null=True)
    fiscalyear_last_month = models.IntegerField()
    tax_calculation_rounding_method = models.CharField(max_length=5, blank=True, null=True)
    localization = models.CharField(max_length=5, blank=True, null=True)
    holding_check_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True, related_name='holding_check_account%(app_label)s_%(class)s_related')
    rejected_check_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True, related_name='rejected_check_account%(app_label)s_%(class)s_related')
    deferred_check_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    sale_note = models.TextField(blank=True, null=True)
    project_time_mode = models.ForeignKey(ProductUom, models.DO_NOTHING, blank=True, null=True)
    internal_transit_location = models.ForeignKey('StockLocation', models.DO_NOTHING, blank=True, null=True)
    propagation_minimum_delta = models.IntegerField(blank=True, null=True)
    po_lead = models.FloatField()
    po_double_validation_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    po_double_validation = models.CharField(max_length=20, blank=True, null=True)
    security_lead = models.FloatField()
    report_company_name = models.CharField(max_length=20, blank=True, null=True)
    internal_notes = models.BooleanField(blank=True, null=True)
    external_notes = models.BooleanField(blank=True, null=True)
    stylesheet = models.ForeignKey(ReportStylesheets, models.DO_NOTHING, blank=True, null=True)
    double_validation = models.BooleanField(blank=True, null=True)
    afip_auth_verify_type = models.CharField(max_length=20)
    sale_allow_vat_no_discrimination = models.CharField(max_length=20, blank=True, null=True)
    automatic_declare_value = models.BooleanField(blank=True, null=True)
    restrict_number_package = models.BooleanField(blank=True, null=True)
    auto_currency_up = models.BooleanField(blank=True, null=True)
    automatic_withholdings = models.BooleanField(blank=True, null=True)
    arba_cit = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_company'


class ResCompanyTablaGananciasRel(models.Model):
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    regimen = models.ForeignKey(AfipTablaGananciasAlicuotasymontos, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_company_tabla_ganancias_rel'
        unique_together = (('company', 'regimen'),)


class ResCompanyUsersRel(models.Model):
    cid = models.ForeignKey(ResCompany, models.DO_NOTHING, db_column='cid')
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_company_users_rel'
        unique_together = (('cid', 'user'),)


class ResConfig(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'res_config'


class ResConfigInstaller(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'res_config_installer'


class ResConfigSettings(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'res_config_settings'


class ResCountry(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    code = models.CharField(unique=True, max_length=2, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    address_format = models.TextField(blank=True, null=True)
    phone_code = models.IntegerField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    cuit_otro = models.CharField(max_length=11, blank=True, null=True)
    afip_code = models.CharField(max_length=3, blank=True, null=True)
    cuit_fisica = models.CharField(max_length=11, blank=True, null=True)
    cuit_juridica = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_country'


class ResCountryGroup(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_country_group'


class ResCountryGroupWebsitePricelistRel(models.Model):
    website_pricelist = models.ForeignKey('WebsitePricelist', models.DO_NOTHING)
    res_country_group = models.ForeignKey(ResCountryGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_country_group_website_pricelist_rel'
        unique_together = (('website_pricelist', 'res_country_group'),)


class ResCountryResCountryGroupRel(models.Model):
    res_country = models.ForeignKey(ResCountry, models.DO_NOTHING)
    res_country_group = models.ForeignKey(ResCountryGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_country_res_country_group_rel'
        unique_together = (('res_country', 'res_country_group'),)


class ResCountryState(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    code = models.CharField(max_length=3)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    country = models.ForeignKey(ResCountry, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    afip_code = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_country_state'


class ResCountryStateResPartnerRel(models.Model):
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    res_country_state = models.ForeignKey(ResCountryState, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_country_state_res_partner_rel'
        unique_together = (('res_partner', 'res_country_state'),)


class ResCurrency(models.Model):
    name = models.CharField(unique=True, max_length=20)
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    rounding = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    symbol = models.CharField(max_length=4, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    position = models.CharField(max_length=20, blank=True, null=True)
    afip_code = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_currency'


class ResCurrencyAutoUpdateRel(models.Model):
    service = models.ForeignKey(CurrencyRateUpdateService, models.DO_NOTHING)
    currency = models.ForeignKey(ResCurrency, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_currency_auto_update_rel'
        unique_together = (('service', 'currency'),)


class ResCurrencyRate(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.DateTimeField()
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    currency = models.ForeignKey(ResCurrency, models.DO_NOTHING, blank=True, null=True)
    rate = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_currency_rate'


class ResCurrencyUpdateAvailRel(models.Model):
    service = models.ForeignKey(CurrencyRateUpdateService, models.DO_NOTHING)
    currency = models.ForeignKey(ResCurrency, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_currency_update_avail_rel'
        unique_together = (('service', 'currency'),)


class ResFont(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    family = models.CharField(max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    mode = models.CharField(max_length=20)
    write_date = models.DateTimeField(blank=True, null=True)
    path = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'res_font'
        unique_together = (('family', 'name'),)


class ResGroups(models.Model):
    comment = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    color = models.IntegerField(blank=True, null=True)
    share = models.BooleanField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey(IrModuleCategory, models.DO_NOTHING, blank=True, null=True)
    is_portal = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_groups'
        unique_together = (('category', 'name'),)


class ResGroupsActionRel(models.Model):
    uid = models.ForeignKey(IrActionsTodo, models.DO_NOTHING, db_column='uid')
    gid = models.ForeignKey(ResGroups, models.DO_NOTHING, db_column='gid')

    class Meta:
        managed = False
        db_table = 'res_groups_action_rel'
        unique_together = (('uid', 'gid'),)


class ResGroupsImpliedRel(models.Model):
    gid = models.ForeignKey(ResGroups, models.DO_NOTHING, db_column='gid', related_name='gid%(app_label)s_%(class)s_related')
    hid = models.ForeignKey(ResGroups, models.DO_NOTHING, db_column='hid', related_name='hid%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'res_groups_implied_rel'
        unique_together = (('gid', 'hid'),)


class ResGroupsReportRel(models.Model):
    uid = models.ForeignKey(IrActReportXml, models.DO_NOTHING, db_column='uid')
    gid = models.ForeignKey(ResGroups, models.DO_NOTHING, db_column='gid')

    class Meta:
        managed = False
        db_table = 'res_groups_report_rel'
        unique_together = (('uid', 'gid'),)


class ResGroupsUsersRel(models.Model):
    gid = models.ForeignKey(ResGroups, models.DO_NOTHING, db_column='gid')
    uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='uid')

    class Meta:
        managed = False
        db_table = 'res_groups_users_rel'
        unique_together = (('gid', 'uid'),)


class ResLang(models.Model):
    name = models.CharField(unique=True, max_length=20)
    code = models.CharField(unique=True, max_length=16)
    date_format = models.CharField(max_length=20)
    direction = models.CharField(max_length=20)
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    thousands_sep = models.CharField(max_length=20, blank=True, null=True)
    translatable = models.BooleanField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    time_format = models.CharField(max_length=20)
    write_date = models.DateTimeField(blank=True, null=True)
    decimal_point = models.CharField(max_length=20)
    active = models.BooleanField(blank=True, null=True)
    iso_code = models.CharField(max_length=16, blank=True, null=True)
    grouping = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'res_lang'


class ResPartner(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    function = models.CharField(max_length=5, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    company_type = models.CharField(max_length=5, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    street = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    display_name = models.CharField(max_length=20, blank=True, null=True)
    zip = models.CharField(max_length=24, blank=True, null=True)
    title = models.ForeignKey('ResPartnerTitle', models.DO_NOTHING, db_column='title', blank=True, null=True)
    country = models.ForeignKey(ResCountry, models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, related_name='parent%(app_label)s_%(class)s_related')
    supplier = models.BooleanField(blank=True, null=True)
    ref = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=20, blank=True, null=True)
    is_company = models.BooleanField(blank=True, null=True)
    website = models.CharField(max_length=20, blank=True, null=True)
    customer = models.BooleanField(blank=True, null=True)
    fax = models.CharField(max_length=10, blank=True, null=True)
    street2 = models.CharField(max_length=30, blank=True, null=True)
    barcode = models.CharField(max_length=30, blank=True, null=True)
    employee = models.BooleanField(blank=True, null=True)
    credit_limit = models.FloatField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    tz = models.CharField(max_length=64, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    lang = models.CharField(max_length=20, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    phone = models.CharField(max_length=10, blank=True, null=True)
    mobile = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=5, blank=True, null=True)
    use_parent_address = models.BooleanField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True, related_name='user%(app_label)s_%(class)s_related')
    birthdate = models.CharField(max_length=10, blank=True, null=True)
    vat = models.CharField(max_length=10, blank=True, null=True)
    state = models.ForeignKey(ResCountryState, models.DO_NOTHING, blank=True, null=True)
    commercial_partner = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, related_name='comercial_partner%(app_label)s_%(class)s_related')
    notify_email = models.CharField(max_length=20)
    message_last_post = models.DateTimeField(blank=True, null=True)
    opt_out = models.BooleanField(blank=True, null=True)
    signup_type = models.CharField(max_length=5, blank=True, null=True)
    signup_expiration = models.DateTimeField(blank=True, null=True)
    signup_token = models.CharField(max_length=5, blank=True, null=True)
    last_time_entries_checked = models.DateTimeField(blank=True, null=True)
    debit_limit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    main_id_number = models.CharField(max_length=10, blank=True, null=True)
    main_id_category = models.ForeignKey('ResPartnerIdCategory', models.DO_NOTHING, blank=True, null=True)
    imp_ganancias_padron = models.CharField(max_length=10, blank=True, null=True)
    gross_income_type = models.CharField(max_length=10, blank=True, null=True)
    gross_income_number = models.CharField(max_length=64, blank=True, null=True)
    actividad_monotributo_padron = models.CharField(max_length=10, blank=True, null=True)
    integrante_soc_padron = models.CharField(max_length=10, blank=True, null=True)
    last_update_padron = models.DateField(blank=True, null=True)
    estado_padron = models.CharField(max_length=10, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    monotributo_padron = models.CharField(max_length=10, blank=True, null=True)
    imp_iva_padron = models.CharField(max_length=10, blank=True, null=True)
    afip_responsability_type = models.ForeignKey('AfipResponsabilityType', models.DO_NOTHING, blank=True, null=True)
    empleador_padron = models.BooleanField(blank=True, null=True)
    team = models.ForeignKey(CrmTeam, models.DO_NOTHING, blank=True, null=True)
    calendar_last_notif_ack = models.DateTimeField(blank=True, null=True)
    last_website_so = models.ForeignKey('SaleOrder', models.DO_NOTHING, blank=True, null=True)
    x_td_visa = models.CharField(max_length=16, blank=True, null=True)
    x_tc_visa = models.CharField(max_length=16, blank=True, null=True)
    x_tc_master = models.CharField(max_length=16, blank=True, null=True)
    x_cbu = models.CharField(max_length=22, blank=True, null=True)
    default_regimen_ganancias = models.ForeignKey(AfipTablaGananciasAlicuotasymontos, models.DO_NOTHING, blank=True, null=True)
    drei = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner'

    
class ResPartnerAfipActivityRel(models.Model):
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING)
    afip_activity = models.ForeignKey(AfipActivity, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_partner_afip_activity_rel'
        unique_together = (('partner', 'afip_activity'),)


class ResPartnerAfipTaxRel(models.Model):
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING)
    afip_tax = models.ForeignKey(AfipTax, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_partner_afip_tax_rel'
        unique_together = (('partner', 'afip_tax'),)


class ResPartnerArbaAlicuot(models.Model):
    numero_comprobante = models.CharField(max_length=20, blank=True, null=True)
    grupo_retencion = models.CharField(max_length=20, blank=True, null=True)
    codigo_hash = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    grupo_percepcion = models.CharField(max_length=20, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    alicuota_retencion = models.FloatField(blank=True, null=True)
    alicuota_percepcion = models.FloatField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING)
    to_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner_arba_alicuot'


class ResPartnerBank(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    bank = models.ForeignKey(ResBank, models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey(ResCurrency, models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sanitized_acc_number = models.CharField(max_length=20, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    acc_number = models.CharField(max_length=20)
    cbu = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner_bank'
        unique_together = (('sanitized_acc_number', 'company'),)


class ResPartnerCategory(models.Model):
    parent_left = models.IntegerField(blank=True, null=True)
    parent_right = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    color = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner_category'


class ResPartnerDocumentTypeRel(models.Model):
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING)
    document_type = models.ForeignKey(AccountDocumentType, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_partner_document_type_rel'
        unique_together = (('partner', 'document_type'),)


class ResPartnerIdCategory(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    code = models.CharField(max_length=16)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    validation_code = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    sequence = models.IntegerField()
    afip_code = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.code)

    class Meta:
        managed = False
        db_table = 'res_partner_id_category'


class ResPartnerIdNumber(models.Model):
    comment = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    valid_from = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    valid_until = models.DateField(blank=True, null=True)
    date_issued = models.DateField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    place_issuance = models.CharField(max_length=20, blank=True, null=True)
    partner_issued = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, related_name='partner%(app_label)s_%(class)s_related')
    category = models.ForeignKey(ResPartnerIdCategory, models.DO_NOTHING)
    sequence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'res_partner_id_number'


class ResPartnerResPartnerCategoryRel(models.Model):
    category = models.ForeignKey(ResPartnerCategory, models.DO_NOTHING)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_partner_res_partner_category_rel'
        unique_together = (('category', 'partner'),)


class ResPartnerTitle(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    shortcut = models.CharField(max_length=20, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner_title'

class ResPartnerNroConector(models.Model):
    secuencia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner_nro_conector'

class ResPartnerUpdateFields(models.Model):
    update = models.ForeignKey('ResPartnerUpdateFromPadronWizard', models.DO_NOTHING)
    field = models.ForeignKey(IrModelFields, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_partner_update_fields'
        unique_together = (('update', 'field'),)


class ResPartnerUpdateFromPadronField(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    old_value = models.CharField(max_length=20, blank=True, null=True)
    wizard = models.ForeignKey('ResPartnerUpdateFromPadronWizard', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    field = models.CharField(max_length=20, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    new_value = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner_update_from_padron_field'


class ResPartnerUpdateFromPadronWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    update_constancia = models.BooleanField(blank=True, null=True)
    title_case = models.BooleanField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    state = models.CharField(max_length=20)
    write_date = models.DateTimeField(blank=True, null=True)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner_update_from_padron_wizard'


class ResRequestLink(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    object = models.CharField(max_length=20)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    priority = models.IntegerField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_request_link'


class ResUsers(models.Model):
    active = models.BooleanField(blank=True, null=True)
    login = models.CharField(unique=True, max_length=64)
    password = models.CharField(max_length=15, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING)
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('self', models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    share = models.BooleanField(blank=True, null=True)
    write_uid = models.ForeignKey('self', models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    signature = models.TextField(blank=True, null=True)
    action_id = models.IntegerField(blank=True, null=True)
    password_crypt = models.CharField(max_length=15, blank=True, null=True)
    alias = models.ForeignKey(MailAlias, models.DO_NOTHING)
    chatter_needaction_auto = models.BooleanField(blank=True, null=True)
    sale_team = models.ForeignKey(CrmTeam, models.DO_NOTHING, blank=True, null=True)
    target_sales_done = models.IntegerField(blank=True, null=True)
    target_sales_won = models.IntegerField(blank=True, null=True)
    target_sales_invoiced = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_users'


class ResUsersLog(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'res_users_log'


class ResUsersWebTipRel(models.Model):
    web_tip = models.ForeignKey('WebTip', models.DO_NOTHING)
    res_users = models.ForeignKey(ResUsers, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_users_web_tip_rel'
        unique_together = (('web_tip', 'res_users'),)


class ResourceCalendar(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    manager = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='manager', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resource_calendar'


class ResourceCalendarAttendance(models.Model):
    dayofweek = models.CharField(max_length=20)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    date_from = models.DateField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    hour_from = models.FloatField()
    hour_to = models.FloatField()
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    calendar = models.ForeignKey(ResourceCalendar, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'resource_calendar_attendance'


class ResourceCalendarLeaves(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    resource = models.ForeignKey('ResourceResource', models.DO_NOTHING, blank=True, null=True)
    date_from = models.DateTimeField()
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateTimeField()
    calendar = models.ForeignKey(ResourceCalendar, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resource_calendar_leaves'


class ResourceResource(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    time_efficiency = models.FloatField()
    code = models.CharField(max_length=16, blank=True, null=True)
    user = models.ForeignKey(ResUsers, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=20)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    calendar = models.ForeignKey(ResourceCalendar, models.DO_NOTHING, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    resource_type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'resource_resource'


class RuleGroupRel(models.Model):
    rule_group = models.ForeignKey(IrRule, models.DO_NOTHING)
    group = models.ForeignKey(ResGroups, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rule_group_rel'
        unique_together = (('rule_group', 'group'),)


class SaleAdvancePaymentInv(models.Model):
    count = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True)
    advance_payment_method = models.CharField(max_length=20)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    deposit_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_advance_payment_inv'


class SaleConfigSettings(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    group_multiple_id_numbers = models.BooleanField(blank=True, null=True)
    unique_id_numbers = models.BooleanField(blank=True, null=True)
    auto_done_setting = models.IntegerField(blank=True, null=True)
    group_display_incoterm = models.IntegerField(blank=True, null=True)
    group_pricelist_item = models.BooleanField(blank=True, null=True)
    group_product_variant = models.IntegerField(blank=True, null=True)
    group_sale_pricelist = models.BooleanField(blank=True, null=True)
    default_invoice_policy = models.CharField(max_length=20, blank=True, null=True)
    group_product_pricelist = models.BooleanField(blank=True, null=True)
    module_website_portal = models.BooleanField(blank=True, null=True)
    module_website_quote = models.IntegerField(blank=True, null=True)
    group_discount_per_so_line = models.IntegerField(blank=True, null=True)
    deposit_product_id_setting = models.ForeignKey(ProductProduct, models.DO_NOTHING, db_column='deposit_product_id_setting', blank=True, null=True)
    module_sale_margin = models.IntegerField(blank=True, null=True)
    sale_pricelist_setting = models.CharField(max_length=20)
    module_website_sale_digital = models.BooleanField(blank=True, null=True)
    group_uom = models.IntegerField(blank=True, null=True)
    group_sale_delivery_address = models.IntegerField(blank=True, null=True)
    module_sale_contract = models.BooleanField(blank=True, null=True)
    module_crm_voip = models.BooleanField(blank=True, null=True)
    alias_domain = models.CharField(max_length=20, blank=True, null=True)
    module_website_sign = models.BooleanField(blank=True, null=True)
    generate_sales_team_alias = models.BooleanField(blank=True, null=True)
    group_use_lead = models.IntegerField(blank=True, null=True)
    alias_prefix = models.CharField(max_length=20, blank=True, null=True)
    module_delivery = models.IntegerField(blank=True, null=True)
    group_mrp_properties = models.IntegerField(blank=True, null=True)
    group_route_so_lines = models.IntegerField(blank=True, null=True)
    default_picking_policy = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_config_settings'


class SaleOrder(models.Model):
    origin = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    team = models.ForeignKey(CrmTeam, models.DO_NOTHING, blank=True, null=True)
    client_order_ref = models.CharField(max_length=20, blank=True, null=True)
    date_order = models.DateTimeField()
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, related_name='partner%(app_label)s_%(class)s_related')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    procurement_group = models.ForeignKey(ProcurementGroup, models.DO_NOTHING, blank=True, null=True)
    amount_untaxed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    pricelist = models.ForeignKey(Product_price_list, models.DO_NOTHING)
    project = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    amount_tax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    validity_date = models.DateField(blank=True, null=True)
    payment_term = models.ForeignKey(AccountPaymentTerm, models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    partner_invoice = models.ForeignKey(ResPartner, models.DO_NOTHING, related_name='partner_invoice%(app_label)s_%(class)s_related')
    user = models.ForeignKey(ResUsers, models.DO_NOTHING, blank=True, null=True)
    fiscal_position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING, blank=True, null=True)
    amount_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    invoice_status = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=20)
    partner_shipping = models.ForeignKey(ResPartner, models.DO_NOTHING)
    campaign = models.ForeignKey('UtmCampaign', models.DO_NOTHING, blank=True, null=True)
    opportunity = models.ForeignKey(CrmLead, models.DO_NOTHING, blank=True, null=True)
    medium = models.ForeignKey('UtmMedium', models.DO_NOTHING, blank=True, null=True)
    source = models.ForeignKey('UtmSource', models.DO_NOTHING, blank=True, null=True)
    picking_policy = models.CharField(max_length=20, blank=True, null=True)
    incoterm = models.ForeignKey('StockIncoterms', models.DO_NOTHING, db_column='incoterm', blank=True, null=True)
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    internal_notes = models.TextField(blank=True, null=True)
    payment_tx = models.ForeignKey(PaymentTransaction, models.DO_NOTHING, blank=True, null=True)
    payment_acquirer = models.ForeignKey(PaymentAcquirer, models.DO_NOTHING, blank=True, null=True)
    carrier = models.ForeignKey(DeliveryCarrier, models.DO_NOTHING, blank=True, null=True)
    delivery_price = models.FloatField(blank=True, null=True)
    invoice_shipping_on_delivery = models.BooleanField(blank=True, null=True)
    todopago_max_insallments = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_order'


class SaleOrderLine(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    qty_to_invoice = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535)
    product_uom_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    qty_invoiced = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    currency = models.ForeignKey(ResCurrency, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    price_tax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product_uom = models.ForeignKey(ProductUom, models.DO_NOTHING, db_column='product_uom')
    customer_lead = models.FloatField()
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    name = models.TextField()
    state = models.CharField(max_length=20, blank=True, null=True)
    order_partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey(SaleOrder, models.DO_NOTHING)
    price_subtotal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    price_reduce = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    qty_delivered = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    invoice_status = models.CharField(max_length=20, blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    salesman = models.ForeignKey(ResUsers, models.DO_NOTHING, blank=True, null=True)
    product_packaging = models.ForeignKey(ProductPackaging, models.DO_NOTHING, db_column='product_packaging', blank=True, null=True)
    route = models.ForeignKey('StockLocationRoute', models.DO_NOTHING, blank=True, null=True)
    is_delivery = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_order_line'


class SaleOrderLineInvoiceRel(models.Model):
    order_line = models.ForeignKey(SaleOrderLine, models.DO_NOTHING)
    invoice_line = models.ForeignKey(AccountInvoiceLine, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sale_order_line_invoice_rel'
        unique_together = (('order_line', 'invoice_line'),)


class SaleOrderTagRel(models.Model):
    order = models.ForeignKey(SaleOrder, models.DO_NOTHING)
    tag = models.ForeignKey(CrmLeadTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sale_order_tag_rel'
        unique_together = (('order', 'tag'),)


class StockBackorderConfirmation(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    pick = models.ForeignKey('StockPicking', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_backorder_confirmation'


class StockBook(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    sequence = models.ForeignKey(IrSequence, models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    lines_per_voucher = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stock_book'


class StockChangeProductQty(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    product_tmpl = models.ForeignKey(ProductTemplate, models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    lot = models.ForeignKey('StockProductionLot', models.DO_NOTHING, blank=True, null=True)
    new_quantity = models.DecimalField(max_digits=65535, decimal_places=65535)
    location = models.ForeignKey('StockLocation', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_change_product_qty'


class StockChangeStandardPrice(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    new_price = models.DecimalField(max_digits=65535, decimal_places=65535)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_change_standard_price'


class StockConfigSettings(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    module_stock_calendar = models.IntegerField(blank=True, null=True)
    group_stock_multiple_locations = models.IntegerField(blank=True, null=True)
    module_stock_picking_wave = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    group_stock_tracking_lot = models.IntegerField(blank=True, null=True)
    group_product_variant = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    module_claim_from_delivery = models.IntegerField(blank=True, null=True)
    module_stock_barcode = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    group_stock_production_lot = models.IntegerField(blank=True, null=True)
    group_stock_tracking_owner = models.IntegerField(blank=True, null=True)
    module_delivery_usps = models.BooleanField(blank=True, null=True)
    module_stock_dropshipping = models.IntegerField(blank=True, null=True)
    module_procurement_jit = models.IntegerField(blank=True, null=True)
    group_stock_packaging = models.IntegerField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    module_delivery_fedex = models.BooleanField(blank=True, null=True)
    decimal_precision = models.IntegerField(blank=True, null=True)
    group_uom = models.IntegerField(blank=True, null=True)
    module_delivery_ups = models.BooleanField(blank=True, null=True)
    module_product_expiry = models.IntegerField(blank=True, null=True)
    group_stock_adv_location = models.IntegerField(blank=True, null=True)
    module_delivery_dhl = models.BooleanField(blank=True, null=True)
    module_stock_landed_costs = models.IntegerField(blank=True, null=True)
    group_stock_inventory_valuation = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_config_settings'


class StockFixedPutawayStrat(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    putaway = models.ForeignKey(ProductPutaway, models.DO_NOTHING)
    sequence = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    fixed_location = models.ForeignKey('StockLocation', models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey(ProductCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_fixed_putaway_strat'


class StockImmediateTransfer(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    pick = models.ForeignKey('StockPicking', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_immediate_transfer'


class StockIncoterms(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    code = models.CharField(max_length=3)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_incoterms'


class StockInventory(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    location = models.ForeignKey('StockLocation', models.DO_NOTHING)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    state = models.CharField(max_length=20, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    lot = models.ForeignKey('StockProductionLot', models.DO_NOTHING, blank=True, null=True)
    date = models.DateTimeField()
    package = models.ForeignKey('StockQuantPackage', models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    filter = models.CharField(max_length=20)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True)
    accounting_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_inventory'


class StockInventoryLine(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    prodlot_name = models.CharField(max_length=20, blank=True, null=True)
    product_name = models.CharField(max_length=20, blank=True, null=True)
    location = models.ForeignKey('StockLocation', models.DO_NOTHING)
    prod_lot = models.ForeignKey('StockProductionLot', models.DO_NOTHING, blank=True, null=True)
    location_name = models.CharField(max_length=20, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    inventory = models.ForeignKey(StockInventory, models.DO_NOTHING, blank=True, null=True)
    package = models.ForeignKey('StockQuantPackage', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    theoretical_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product_uom = models.ForeignKey(ProductUom, models.DO_NOTHING)
    product_code = models.CharField(max_length=20, blank=True, null=True)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_inventory_line'


class StockLocation(models.Model):
    parent_left = models.IntegerField(blank=True, null=True)
    parent_right = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    putaway_strategy = models.ForeignKey(ProductPutaway, models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    location = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    removal_strategy = models.ForeignKey(ProductRemoval, models.DO_NOTHING, blank=True, null=True)
    scrap_location = models.BooleanField(blank=True, null=True)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    complete_name = models.CharField(max_length=20, blank=True, null=True)
    usage = models.CharField(max_length=20)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    barcode = models.CharField(max_length=20, blank=True, null=True)
    posz = models.IntegerField(blank=True, null=True)
    posx = models.IntegerField(blank=True, null=True)
    posy = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=20)
    return_location = models.BooleanField(blank=True, null=True)
    valuation_in_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True, related_name='valuation_in_account%(app_label)s_%(class)s_related')
    valuation_out_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True, related_name='valuation_out_account%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'stock_location'
        unique_together = (('barcode', 'company'),)


class StockLocationPath(models.Model):
    location_from = models.ForeignKey(StockLocation, models.DO_NOTHING, related_name='location_from%(app_label)s_%(class)s_related')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    route_sequence = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING)
    auto = models.CharField(max_length=20)
    sequence = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    delay = models.IntegerField(blank=True, null=True)
    route = models.ForeignKey('StockLocationRoute', models.DO_NOTHING, blank=True, null=True)
    location_dest = models.ForeignKey(StockLocation, models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    propagate = models.BooleanField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'stock_location_path'


class StockLocationRoute(models.Model):
    supplier_wh = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True, related_name='supplier_wh%(app_label)s_%(class)s_related')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    sequence = models.IntegerField(blank=True, null=True)
    warehouse_selectable = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    supplied_wh = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    product_selectable = models.BooleanField(blank=True, null=True)
    product_categ_selectable = models.BooleanField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    sale_selectable = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_location_route'


class StockLocationRouteCateg(models.Model):
    route = models.ForeignKey(StockLocationRoute, models.DO_NOTHING)
    categ = models.ForeignKey(ProductCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_location_route_categ'
        unique_together = (('route', 'categ'),)


class StockLocationRouteMove(models.Model):
    move = models.ForeignKey('StockMove', models.DO_NOTHING)
    route = models.ForeignKey(StockLocationRoute, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_location_route_move'
        unique_together = (('move', 'route'),)


class StockLocationRouteProcurement(models.Model):
    procurement = models.ForeignKey(ProcurementOrder, models.DO_NOTHING)
    route = models.ForeignKey(StockLocationRoute, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_location_route_procurement'
        unique_together = (('procurement', 'route'),)


class StockMove(models.Model):
    origin = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    move_dest = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, related_name='move_dest%(app_label)s_%(class)s_related')
    product_uom = models.ForeignKey(ProductUom, models.DO_NOTHING, db_column='product_uom', related_name='product_uom%(app_label)s_%(class)s_related')
    price_unit = models.FloatField(blank=True, null=True)
    product_uom_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    date = models.DateTimeField()
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    location = models.ForeignKey(StockLocation, models.DO_NOTHING, related_name='location%(app_label)s_%(class)s_related')
    priority = models.CharField(max_length=20, blank=True, null=True)
    picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    origin_returned_move = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, related_name='origin_returned_move%(app_label)s_%(class)s_related')
    product_packaging = models.ForeignKey(ProductPackaging, models.DO_NOTHING, db_column='product_packaging', blank=True, null=True)
    date_expected = models.DateTimeField()
    procurement = models.ForeignKey(ProcurementOrder, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=20)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    inventory = models.ForeignKey(StockInventory, models.DO_NOTHING, blank=True, null=True)
    partially_available = models.BooleanField(blank=True, null=True)
    propagate = models.BooleanField(blank=True, null=True)
    restrict_partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True, related_name='restrict_partner%(app_label)s_%(class)s_related')
    procure_method = models.CharField(max_length=20)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    restrict_lot = models.ForeignKey('StockProductionLot', models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    group = models.ForeignKey(ProcurementGroup, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    split_from = models.ForeignKey('self', models.DO_NOTHING, db_column='split_from', blank=True, null=True)
    picking = models.ForeignKey('StockPicking', models.DO_NOTHING, blank=True, null=True)
    location_dest = models.ForeignKey(StockLocation, models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    push_rule = models.ForeignKey(StockLocationPath, models.DO_NOTHING, blank=True, null=True)
    rule = models.ForeignKey(ProcurementRule, models.DO_NOTHING, blank=True, null=True)
    purchase_line = models.ForeignKey(PurchaseOrderLine, models.DO_NOTHING, blank=True, null=True)
    weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    weight_uom = models.ForeignKey(ProductUom, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_move'


class StockMoveOperationLink(models.Model):
    reserved_quant = models.ForeignKey('StockQuant', models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    qty = models.FloatField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    operation = models.ForeignKey('StockPackOperation', models.DO_NOTHING)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    move = models.ForeignKey(StockMove, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_move_operation_link'


class StockMoveScrap(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    product_uom = models.ForeignKey(ProductUom, models.DO_NOTHING, db_column='product_uom')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    location = models.ForeignKey(StockLocation, models.DO_NOTHING)
    restrict_lot = models.ForeignKey('StockProductionLot', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_move_scrap'


class StockPackOperation(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    result_package = models.ForeignKey('StockQuantPackage', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    package = models.ForeignKey('StockQuantPackage', models.DO_NOTHING, blank=True, null=True, related_name='package%(app_label)s_%(class)s_related')
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    location = models.ForeignKey(StockLocation, models.DO_NOTHING, related_name='location%(app_label)s_%(class)s_related')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    qty_done = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    owner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    fresh_record = models.BooleanField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField()
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True)
    product_uom = models.ForeignKey(ProductUom, models.DO_NOTHING, blank=True, null=True)
    location_dest = models.ForeignKey(StockLocation, models.DO_NOTHING)
    picking = models.ForeignKey('StockPicking', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_pack_operation'


class StockPackOperationLot(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    lot_name = models.CharField(max_length=20, blank=True, null=True)
    qty_todo = models.FloatField(blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    lot = models.ForeignKey('StockProductionLot', models.DO_NOTHING, blank=True, null=True)
    operation = models.ForeignKey(StockPackOperation, models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'stock_pack_operation_lot'
        unique_together = (('operation', 'lot_name'), ('operation', 'lot'),)


class StockPicking(models.Model):
    origin = models.CharField(max_length=20, blank=True, null=True)
    date_done = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    launch_pack_operations = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True, related_name='partner%(app_label)s_%(class)s_related')
    backorder = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    priority = models.CharField(max_length=20)
    picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING)
    location = models.ForeignKey(StockLocation, models.DO_NOTHING, related_name='location%(app_label)s_%(class)s_related')
    move_type = models.CharField(max_length=20)
    message_last_post = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    note = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    owner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    min_date = models.DateTimeField(blank=True, null=True)
    printed = models.BooleanField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    recompute_pack_op = models.BooleanField(blank=True, null=True)
    location_dest = models.ForeignKey(StockLocation, models.DO_NOTHING)
    max_date = models.DateTimeField(blank=True, null=True)
    group = models.ForeignKey(ProcurementGroup, models.DO_NOTHING, blank=True, null=True)
    carrier_tracking_ref = models.CharField(max_length=20, blank=True, null=True)
    number_of_packages = models.IntegerField(blank=True, null=True)
    carrier = models.ForeignKey(DeliveryCarrier, models.DO_NOTHING, blank=True, null=True)
    weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    weight_uom = models.ForeignKey(ProductUom, models.DO_NOTHING)
    volume = models.FloatField(blank=True, null=True)
    carrier_price = models.FloatField(blank=True, null=True)
    observations = models.TextField(blank=True, null=True)
    declared_value = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    book = models.ForeignKey(StockBook, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_picking'
        unique_together = (('name', 'company'),)


class StockPickingType(models.Model):
    code = models.CharField(max_length=20)
    create_date = models.DateTimeField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    use_create_lots = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    default_location_dest = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True, related_name='stock_default_dest%(app_label)s_%(class)s_related')
    show_entire_packs = models.BooleanField(blank=True, null=True)
    barcode_nomenclature = models.ForeignKey(BarcodeNomenclature, models.DO_NOTHING, blank=True, null=True)
    use_existing_lots = models.BooleanField(blank=True, null=True)
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    sequence_0 = models.ForeignKey(IrSequence, models.DO_NOTHING, db_column='sequence_id')  # Field renamed because of name conflict.
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=20)
    return_picking_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    default_location_src = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True, related_name='stock_default_src%(app_label)s_%(class)s_related')
    book_required = models.BooleanField(blank=True, null=True)
    pricelist = models.ForeignKey(Product_price_list, models.DO_NOTHING, blank=True, null=True)
    voucher_number_unique = models.BooleanField(blank=True, null=True)
    voucher_required = models.BooleanField(blank=True, null=True)
    book = models.ForeignKey(StockBook, models.DO_NOTHING, blank=True, null=True)
    voucher_number_validator = models.ForeignKey(BaseValidator, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_picking_type'


class StockPickingVoucher(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    write_date = models.DateTimeField(blank=True, null=True)
    picking = models.ForeignKey(StockPicking, models.DO_NOTHING)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    book = models.ForeignKey(StockBook, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_picking_voucher'
        unique_together = (('name', 'book'),)


class StockPrintStockVoucher(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    estimated_number_of_pages = models.IntegerField(blank=True, null=True)
    book = models.ForeignKey(StockBook, models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    picking = models.ForeignKey(StockPicking, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_print_stock_voucher'


class StockProductionLot(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    message_last_post = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    ref = models.CharField(max_length=20, blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_production_lot'
        unique_together = (('name', 'product'),)


class StockQuant(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    propagated_from = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    package = models.ForeignKey('StockQuantPackage', models.DO_NOTHING, blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    lot = models.ForeignKey(StockProductionLot, models.DO_NOTHING, blank=True, null=True)
    reservation = models.ForeignKey(StockMove, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    location = models.ForeignKey(StockLocation, models.DO_NOTHING)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    owner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    qty = models.FloatField()
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    packaging_type = models.ForeignKey(ProductPackaging, models.DO_NOTHING, blank=True, null=True)
    negative_move = models.ForeignKey(StockMove, models.DO_NOTHING, blank=True, null=True, related_name='negative_move%(app_label)s_%(class)s_related')
    in_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_quant'


class StockQuantMoveRel(models.Model):
    quant = models.ForeignKey(StockQuant, models.DO_NOTHING)
    move = models.ForeignKey(StockMove, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_quant_move_rel'
        unique_together = (('quant', 'move'),)


class StockQuantPackage(models.Model):
    parent_left = models.IntegerField(blank=True, null=True)
    parent_right = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    packaging = models.ForeignKey(ProductPackaging, models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_quant_package'


class StockReturnPicking(models.Model):
    move_dest_exists = models.BooleanField(blank=True, null=True)
    original_location = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    parent_location = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True, related_name='parent_location%(app_label)s_%(class)s_related')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    location = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True, related_name='location%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'stock_return_picking'


class StockReturnPickingLine(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    wizard = models.ForeignKey(StockReturnPicking, models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    move = models.ForeignKey(StockMove, models.DO_NOTHING, blank=True, null=True)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'stock_return_picking_line'


class StockRouteProduct(models.Model):
    route = models.ForeignKey(StockLocationRoute, models.DO_NOTHING)
    product = models.ForeignKey(ProductTemplate, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_route_product'
        unique_together = (('route', 'product'),)


class StockRouteWarehouse(models.Model):
    route = models.ForeignKey(StockLocationRoute, models.DO_NOTHING)
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_route_warehouse'
        unique_together = (('route', 'warehouse'),)


class StockWarehouse(models.Model):
    crossdock_route = models.ForeignKey(StockLocationRoute, models.DO_NOTHING, blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    lot_stock = models.ForeignKey(StockLocation, models.DO_NOTHING, related_name='lot_stock%(app_label)s_%(class)s_related')
    wh_pack_stock_loc = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True, related_name='wh_pack_stock_loc%(app_label)s_%(class)s_related')
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    pick_type = models.ForeignKey(StockPickingType, models.DO_NOTHING, blank=True, null=True, related_name='pick_type%(app_label)s_%(class)s_related')
    code = models.CharField(max_length=5)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    mto_pull = models.ForeignKey(ProcurementRule, models.DO_NOTHING, blank=True, null=True, related_name='mto_pull%(app_label)s_%(class)s_related')
    reception_route = models.ForeignKey(StockLocationRoute, models.DO_NOTHING, blank=True, null=True, related_name='reception_route%(app_label)s_%(class)s_related')
    wh_input_stock_loc = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True)
    delivery_steps = models.CharField(max_length=20)
    default_resupply_wh = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    view_location = models.ForeignKey(StockLocation, models.DO_NOTHING, related_name='view_location%(app_label)s_%(class)s_related' )
    wh_qc_stock_loc = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True, related_name='wh_qc_stock_loc%(app_label)s_%(class)s_related' )
    reception_steps = models.CharField(max_length=20)
    resupply_from_wh = models.BooleanField(blank=True, null=True)
    pack_type = models.ForeignKey(StockPickingType, models.DO_NOTHING, blank=True, null=True)
    wh_output_stock_loc = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True, related_name='wh_output_stock_loc%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    delivery_route = models.ForeignKey(StockLocationRoute, models.DO_NOTHING, blank=True, null=True, related_name='delivery_route%(app_label)s_%(class)s_related')
    name = models.CharField(max_length=20)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    in_type = models.ForeignKey(StockPickingType, models.DO_NOTHING, blank=True, null=True, related_name='in_type%(app_label)s_%(class)s_related')
    out_type = models.ForeignKey(StockPickingType, models.DO_NOTHING, blank=True, null=True, related_name='out_type%(app_label)s_%(class)s_related')
    int_type = models.ForeignKey(StockPickingType, models.DO_NOTHING, blank=True, null=True, related_name='int_type%(app_label)s_%(class)s_related')
    buy_pull = models.ForeignKey(ProcurementRule, models.DO_NOTHING, blank=True, null=True)
    buy_to_resupply = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_warehouse'
        unique_together = (('code', 'company'), ('name', 'company'),)


class StockWarehouseOrderpoint(models.Model):
    product_max_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    qty_multiple = models.DecimalField(max_digits=65535, decimal_places=65535)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    location = models.ForeignKey(StockLocation, models.DO_NOTHING)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    active = models.BooleanField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    lead_type = models.CharField(max_length=20)
    group = models.ForeignKey(ProcurementGroup, models.DO_NOTHING, blank=True, null=True)
    warehouse = models.ForeignKey(StockWarehouse, models.DO_NOTHING)
    product_min_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    lead_days = models.IntegerField(blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_warehouse_orderpoint'


class StockWhResupplyTable(models.Model):
    supplied_wh = models.ForeignKey(StockWarehouse, models.DO_NOTHING, related_name='supplied_wh%(app_label)s_%(class)s_related')
    supplier_wh = models.ForeignKey(StockWarehouse, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_wh_resupply_table'
        unique_together = (('supplied_wh', 'supplier_wh'),)


class SurveyLabel(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    question_id_2 = models.ForeignKey('SurveyQuestion', models.DO_NOTHING, db_column='question_id_2', blank=True, null=True, related_name='question_id_2%(app_label)s_%(class)s_related')
    sequence = models.IntegerField(blank=True, null=True)
    quizz_mark = models.FloatField(blank=True, null=True)
    value = models.CharField(max_length=20)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    question = models.ForeignKey('SurveyQuestion', models.DO_NOTHING, blank=True, null=True, related_name='question%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'survey_label'


class SurveyMailComposeMessage(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    no_auto_thread = models.BooleanField(blank=True, null=True)
    mail_server = models.ForeignKey(IrMailServer, models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    notify = models.BooleanField(blank=True, null=True)
    email_from = models.CharField(max_length=20, blank=True, null=True)
    active_domain = models.TextField(blank=True, null=True)
    subject = models.CharField(max_length=20, blank=True, null=True)
    composition_mode = models.CharField(max_length=20, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    multi_email = models.TextField(blank=True, null=True)
    is_log = models.BooleanField(blank=True, null=True)
    parent = models.ForeignKey(MailMessage, models.DO_NOTHING, blank=True, null=True)
    subtype = models.ForeignKey(MailMessageSubtype, models.DO_NOTHING, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    message_id = models.CharField(max_length=20, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    record_name = models.CharField(max_length=20, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    model = models.CharField(max_length=20, blank=True, null=True)
    use_active_domain = models.BooleanField(blank=True, null=True)
    date_deadline = models.DateField(blank=True, null=True)
    public = models.CharField(max_length=20)
    reply_to = models.CharField(max_length=20, blank=True, null=True)
    author = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    survey = models.ForeignKey('SurveySurvey', models.DO_NOTHING)
    message_type = models.CharField(max_length=20)
    template = models.ForeignKey(MailTemplate, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_mail_compose_message'


class SurveyMailComposeMessageIrAttachmentsRel(models.Model):
    wizard = models.ForeignKey(SurveyMailComposeMessage, models.DO_NOTHING)
    attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'survey_mail_compose_message_ir_attachments_rel'
        unique_together = (('wizard', 'attachment'),)


class SurveyMailComposeMessageResPartnerRel(models.Model):
    wizard = models.ForeignKey(SurveyMailComposeMessage, models.DO_NOTHING)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'survey_mail_compose_message_res_partner_rel'
        unique_together = (('wizard', 'partner'),)


class SurveyPage(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=20)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    survey = models.ForeignKey('SurveySurvey', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'survey_page'


class SurveyQuestion(models.Model):
    constr_error_msg = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    matrix_subtype = models.CharField(max_length=20, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    comments_allowed = models.BooleanField(blank=True, null=True)
    validation_min_float_value = models.FloatField(blank=True, null=True)
    constr_mandatory = models.BooleanField(blank=True, null=True)
    column_nb = models.CharField(max_length=20, blank=True, null=True)
    validation_required = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    validation_length_max = models.IntegerField(blank=True, null=True)
    validation_length_min = models.IntegerField(blank=True, null=True)
    question = models.CharField(max_length=20)
    display_mode = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=15)
    validation_min_date = models.DateTimeField(blank=True, null=True)
    comments_message = models.CharField(max_length=20, blank=True, null=True)
    validation_email = models.BooleanField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    comment_count_as_answer = models.BooleanField(blank=True, null=True)
    validation_max_float_value = models.FloatField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    validation_max_date = models.DateTimeField(blank=True, null=True)
    validation_error_msg = models.CharField(max_length=20, blank=True, null=True)
    page = models.ForeignKey(SurveyPage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'survey_question'


class SurveyStage(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    sequence = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    fold = models.BooleanField(blank=True, null=True)
    closed = models.BooleanField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_stage'


class SurveySurvey(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    thank_you_message = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    quizz_mode = models.BooleanField(blank=True, null=True)
    users_can_go_back = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    auth_required = models.BooleanField(blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    email_template = models.ForeignKey(MailTemplate, models.DO_NOTHING, blank=True, null=True)
    stage = models.ForeignKey(SurveyStage, models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'survey_survey'


class SurveyUserInput(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    date_create = models.DateTimeField()
    email = models.CharField(max_length=20, blank=True, null=True)
    token = models.CharField(unique=True, max_length=20)
    deadline = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    last_displayed_page = models.ForeignKey(SurveyPage, models.DO_NOTHING, blank=True, null=True)
    survey = models.ForeignKey(SurveySurvey, models.DO_NOTHING)
    type = models.CharField(max_length=20)
    test_entry = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_user_input'


class SurveyUserInputLine(models.Model):
    value_date = models.DateTimeField(blank=True, null=True)
    value_suggested_row = models.ForeignKey(SurveyLabel, models.DO_NOTHING, db_column='value_suggested_row', blank=True, null=True, related_name='value_suggested_row%(app_label)s_%(class)s_related')
    skipped = models.BooleanField(blank=True, null=True)
    value_suggested = models.ForeignKey(SurveyLabel, models.DO_NOTHING, db_column='value_suggested', blank=True, null=True, related_name='value_suggested%(app_label)s_%(class)s_related')
    answer_type = models.CharField(max_length=20, blank=True, null=True)
    value_text = models.CharField(max_length=20, blank=True, null=True)
    quizz_mark = models.FloatField(blank=True, null=True)
    user_input = models.ForeignKey(SurveyUserInput, models.DO_NOTHING)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    date_create = models.DateTimeField()
    value_number = models.FloatField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    survey = models.ForeignKey(SurveySurvey, models.DO_NOTHING, blank=True, null=True)
    value_free_text = models.TextField(blank=True, null=True)
    question = models.ForeignKey(SurveyQuestion, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'survey_user_input_line'


class UtmCampaign(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utm_campaign'


class UtmMedium(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utm_medium'


class UtmSource(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utm_source'


class ValidateAccountMove(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'validate_account_move'


class WebEditorConverterTest(models.Model):
    binary = models.BinaryField(blank=True, null=True)
    selection = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    text = models.TextField(blank=True, null=True)
    float = models.FloatField(blank=True, null=True)
    numeric = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
    char = models.CharField(max_length=20, blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    selection_str = models.CharField(max_length=20, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    many2one = models.ForeignKey('WebEditorConverterTestSub', models.DO_NOTHING, db_column='many2one', blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    integer = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'web_editor_converter_test'


class WebEditorConverterTestSub(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_editor_converter_test_sub'


class WebPlanner(models.Model):
    menu = models.ForeignKey(IrUiMenu, models.DO_NOTHING)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    planner_application = models.CharField(max_length=20)
    view = models.ForeignKey(IrUiView, models.DO_NOTHING)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    progress = models.IntegerField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    tooltip_planner = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_planner'


class WebTip(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    placement = models.CharField(max_length=20, blank=True, null=True)
    end_selector = models.CharField(max_length=20, blank=True, null=True)
    title = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField()
    end_event = models.CharField(max_length=20, blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    mode = models.CharField(max_length=20, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    trigger_selector = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    model = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    highlight_selector = models.CharField(max_length=20, blank=True, null=True)
    action = models.ForeignKey(IrActWindow, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_tip'


class Website(models.Model):
    domain = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    social_linkedin = models.CharField(max_length=20, blank=True, null=True)
    cdn_filters = models.TextField(blank=True, null=True)
    social_facebook = models.CharField(max_length=20, blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    google_analytics_key = models.CharField(max_length=20, blank=True, null=True)
    default_lang = models.ForeignKey(ResLang, models.DO_NOTHING)
    social_twitter = models.CharField(max_length=20, blank=True, null=True)
    cdn_url = models.CharField(max_length=20, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    user = models.ForeignKey(ResUsers, models.DO_NOTHING, related_name='user%(app_label)s_%(class)s_related')
    default_lang_code = models.CharField(max_length=20, blank=True, null=True)
    social_googleplus = models.CharField(max_length=20, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    social_github = models.CharField(max_length=20, blank=True, null=True)
    compress_html = models.BooleanField(blank=True, null=True)
    social_youtube = models.CharField(max_length=20, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    cdn_activated = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    salesteam = models.ForeignKey(CrmTeam, models.DO_NOTHING, blank=True, null=True)
    salesperson = models.ForeignKey(ResUsers, models.DO_NOTHING, blank=True, null=True, related_name='salesperson%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'website'


class WebsiteConfigSettings(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    website = models.ForeignKey(Website, models.DO_NOTHING)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    module_website_version = models.BooleanField(blank=True, null=True)
    module_website_form_editor = models.BooleanField(blank=True, null=True)
    module_delivery_usps = models.BooleanField(blank=True, null=True)
    module_delivery_fedex = models.BooleanField(blank=True, null=True)
    module_delivery_ups = models.BooleanField(blank=True, null=True)
    module_sale_ebay = models.BooleanField(blank=True, null=True)
    module_delivery_dhl = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'website_config_settings'


class WebsiteLangRel(models.Model):
    website = models.ForeignKey(Website, models.DO_NOTHING)
    lang = models.ForeignKey(ResLang, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'website_lang_rel'
        unique_together = (('website', 'lang'),)


class WebsiteMenu(models.Model):
    parent_left = models.IntegerField(blank=True, null=True)
    parent_right = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    sequence = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=20, blank=True, null=True)
    website = models.ForeignKey(Website, models.DO_NOTHING, blank=True, null=True)
    new_window = models.BooleanField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'website_menu'


class WebsitePricelist(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    website = models.ForeignKey(Website, models.DO_NOTHING)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    pricelist = models.ForeignKey(Product_price_list, models.DO_NOTHING, blank=True, null=True)
    selectable = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'website_pricelist'


class WebsiteSeoMetadata(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    website_meta_description = models.TextField(blank=True, null=True)
    website_meta_title = models.CharField(max_length=20, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    website_meta_keywords = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'website_seo_metadata'


class WizardIrModelMenuCreate(models.Model):
    menu = models.ForeignKey(IrUiMenu, models.DO_NOTHING)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wizard_ir_model_menu_create'


class WizardMultiChartsAccounts(models.Model):
    only_one_chart_template = models.BooleanField(blank=True, null=True)
    bank_account_code_prefix = models.CharField(max_length=20, blank=True, null=True)
    cash_account_code_prefix = models.CharField(max_length=20, blank=True, null=True)
    code_digits = models.IntegerField()
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    transfer_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING)
    purchase_tax = models.ForeignKey(AccountTaxTemplate, models.DO_NOTHING, blank=True, null=True, related_name='purchase_tax%(app_label)s_%(class)s_related')
    chart_template = models.ForeignKey(AccountChartTemplate, models.DO_NOTHING)
    complete_tax_set = models.BooleanField(blank=True, null=True)
    sale_tax = models.ForeignKey(AccountTaxTemplate, models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    currency = models.ForeignKey(ResCurrency, models.DO_NOTHING)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    purchase_tax_rate = models.FloatField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sale_tax_rate = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wizard_multi_charts_accounts'


class WizardValuationHistory(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField()
    choose_date = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wizard_valuation_history'


class Wkf(models.Model):
    name = models.CharField(max_length=20)
    osv = models.CharField(max_length=20)
    on_create = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'wkf'


class WkfActivity(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    kind = models.CharField(max_length=20)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20)
    join_mode = models.CharField(max_length=3)
    flow_stop = models.BooleanField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    subflow = models.ForeignKey(Wkf, models.DO_NOTHING, blank=True, null=True, related_name='subflow%(app_label)s_%(class)s_related')
    split_mode = models.CharField(max_length=3)
    write_date = models.DateTimeField(blank=True, null=True)
    action = models.TextField(blank=True, null=True)
    wkf = models.ForeignKey(Wkf, models.DO_NOTHING, related_name='wkf%(app_label)s_%(class)s_related')
    signal_send = models.CharField(max_length=20, blank=True, null=True)
    flow_start = models.BooleanField(blank=True, null=True)
    action_0 = models.ForeignKey(IrActServer, models.DO_NOTHING, db_column='action_id', blank=True, null=True)  # Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'wkf_activity'


class WkfInstance(models.Model):
    res_type = models.CharField(max_length=20, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    wkf = models.ForeignKey(Wkf, models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=10, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wkf_instance'


class WkfTransition(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True, related_name='create_uid%(app_label)s_%(class)s_related')
    create_date = models.DateTimeField(blank=True, null=True)
    trigger_model = models.CharField(max_length=20, blank=True, null=True)
    signal = models.CharField(max_length=20, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True, related_name='write_uid%(app_label)s_%(class)s_related')
    act_from = models.ForeignKey(WkfActivity, models.DO_NOTHING, db_column='act_from', related_name='act_from%(app_label)s_%(class)s_related')
    condition = models.CharField(max_length=20)
    write_date = models.DateTimeField(blank=True, null=True)
    trigger_expr_id = models.CharField(max_length=20, blank=True, null=True)
    group = models.ForeignKey(ResGroups, models.DO_NOTHING, blank=True, null=True)
    act_to = models.ForeignKey(WkfActivity, models.DO_NOTHING, db_column='act_to', related_name='act_to%(app_label)s_%(class)s_related')

    class Meta:
        managed = False
        db_table = 'wkf_transition'


class WkfTriggers(models.Model):
    instance = models.ForeignKey(WkfInstance, models.DO_NOTHING, blank=True, null=True)
    workitem = models.ForeignKey('WkfWorkitem', models.DO_NOTHING, related_name='workitem%(app_label)s_%(class)s_related')
    model = models.CharField(max_length=20, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wkf_triggers'


class WkfWitmTrans(models.Model):
    inst = models.ForeignKey(WkfInstance, models.DO_NOTHING)
    trans = models.ForeignKey(WkfTransition, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wkf_witm_trans'
        unique_together = (('inst', 'trans'),)


class WkfWorkitem(models.Model):
    act = models.ForeignKey(WkfActivity, models.DO_NOTHING)
    inst = models.ForeignKey(WkfInstance, models.DO_NOTHING, related_name='inst%(app_label)s_%(class)s_related')
    subflow = models.ForeignKey(WkfInstance, models.DO_NOTHING, blank=True, null=True, related_name='subflow%(app_label)s_%(class)s_related')
    state = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wkf_workitem'


