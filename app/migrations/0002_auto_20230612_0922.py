# Generated by Django 2.2.28 on 2023-06-12 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clr',
            name='age_of_unpaid_obligation_days',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='approved_amount_original_ccy',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='approved_amount_usd',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='br',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='business_unit_division',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='cap_era_interest_rates',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='cbk_grade',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='collateral_desc',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='collateral_status',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='collateral_type',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='collateral_value_kes',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='collateral_value_usd',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='currency_short_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='currency_type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='current_exposure_original_ccy',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='current_exposure_usd',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='current_valuation_date',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='cust_id',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='cust_id1',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='customer_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='customer_type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='date_of_last_credit',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='exposure_type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='facility_description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='facility_type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='fx_rate',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='group_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='group_name1',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='ifrs_classification',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='impairment_usd',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='installment',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='int_rate',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='last_3month_credit',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='last_credit_amount',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='location',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='maturity_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='obligor_risk_rating',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='one_month_collection',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='outstanding_balance_usd',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='product',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='prudential_classification',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='ref_no',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='sector',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='settlement_account',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='sn',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='tenor',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='three_months_collections',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='unpaid_amount_ghc_missed',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='unpaid_amount_usd',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='unpaid_installment',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='clr',
            name='value_date',
            field=models.DateTimeField(null=True),
        ),
    ]