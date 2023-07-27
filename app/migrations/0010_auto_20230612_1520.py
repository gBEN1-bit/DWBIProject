# Generated by Django 2.2.28 on 2023-06-12 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20230612_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewCLR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('S_N', models.FloatField(db_column='S_N', null=True)),
                ('CUST_ID', models.CharField(max_length=255, null=True)),
                ('CUSTOMER_NAME', models.CharField(max_length=255, null=True)),
                ('CUST_ID1', models.CharField(max_length=255, null=True)),
                ('CUSTOMER_TYPE', models.CharField(max_length=255, null=True)),
                ('REF_NO', models.CharField(max_length=255, null=True)),
                ('BR', models.CharField(max_length=255, null=True)),
                ('LOCATION', models.CharField(max_length=255, null=True)),
                ('PRODUCT', models.CharField(max_length=255, null=True)),
                ('SETTLEMENT_ACCOUNT', models.CharField(max_length=255, null=True)),
                ('FACILITY_DESCRIPTION', models.CharField(max_length=255, null=True)),
                ('FACILITY_TYPE', models.CharField(max_length=255, null=True)),
                ('EXPOSURE_TYPE', models.CharField(max_length=255, null=True)),
                ('CURRENCY_SHORT_NAME', models.CharField(max_length=255, null=True)),
                ('CURRENCY_TYPE', models.CharField(max_length=255, null=True)),
                ('SECTOR', models.CharField(max_length=255, null=True)),
                ('OBLIGOR_RISK_RATING', models.CharField(max_length=255, null=True)),
                ('CBK_GRADE', models.FloatField(db_column='CBK_GRADE', null=True)),
                ('PRUDENTIAL_CLASSIFICATION', models.CharField(max_length=255, null=True)),
                ('IFRS_CLASSIFICATION', models.CharField(max_length=255, null=True)),
                ('FX_RATE', models.CharField(max_length=255, null=True)),
                ('APPROVED_AMOUNT_ORIGINAL_CCY', models.FloatField(db_column='APPROVED_AMOUNT_ORIGINAL_CCY', null=True)),
                ('APPROVED_AMOUNT_USD', models.FloatField(db_column='APPROVED_AMOUNT_USD', null=True)),
                ('OUTSTANDING_BALANCE_USD', models.FloatField(db_column='OUTSTANDING_BALANCE_USD', null=True)),
                ('CURRENT_EXPOSURE_ORIGINAL_CCY', models.FloatField(db_column='CURRENT_EXPOSURE_ORIGINAL_CCY', null=True)),
                ('CURRENT_EXPOSURE_USD', models.FloatField(db_column='CURRENT_EXPOSURE_USD', null=True)),
                ('VALUE_DATE', models.DateTimeField(null=True)),
                ('MATURITY_DATE', models.DateTimeField(null=True)),
                ('INT_RATE', models.FloatField(null=True)),
                ('CAP_ERA_INTEREST_RATES', models.CharField(db_column='CAP_ERA_INTEREST_RATES', max_length=255, null=True)),
                ('TENOR', models.FloatField(null=True)),
                ('IMPAIRMENT_USD', models.FloatField(db_column='IMPAIRMENT_USD', null=True)),
                ('DATE_OF_LAST_CREDIT', models.DateTimeField(db_column='DATE_OF_LAST_CREDIT', null=True)),
                ('LAST_CREDIT_AMOUNT', models.FloatField(db_column='LAST_CREDIT_AMOUNT', null=True)),
                ('INSTALLMENT', models.FloatField(null=True)),
                ('AGE_OF_UNPAID_OBLIGATION_DAYS', models.FloatField(db_column='AGE_OF_UNPAID_OBLIGATION_DAYS', null=True)),
                ('UNPAID_AMOUNT_USD', models.FloatField(db_column='UNPAID_AMOUNT_USD', null=True)),
                ('UNPAID_AMOUNT_GHC_MISSED', models.FloatField(db_column='UNPAID_AMOUNT_GHC_MISSED', null=True)),
                ('UNPAID_INSTALLMENT', models.FloatField(null=True)),
                ('ONE_MONTH_COLLECTION', models.FloatField(db_column='1_MONTH_COLLECTION', null=True)),
                ('THREE_MONTHS_COLLECTIONS', models.CharField(db_column='3_MONTHS_COLLECTIONS', max_length=255, null=True)),
                ('LAST_3MONTH_CREDIT', models.FloatField(null=True)),
                ('COLLATERAL_TYPE', models.TextField(null=True)),
                ('COLLATERAL_STATUS', models.CharField(max_length=255, null=True)),
                ('COLLATERAL_VALUE_KES', models.FloatField(db_column='COLLATERAL_VALUE_KES', null=True)),
                ('COLLATERAL_VALUE_USD', models.CharField(db_column='COLLATERAL_VALUE_USD', max_length=255, null=True)),
                ('COLLATERAL_DESC', models.TextField(null=True)),
                ('CURRENT_VALUATION_DATE', models.CharField(max_length=255, null=True)),
                ('BUSINESS_UNIT_DIVISION', models.CharField(db_column='BUSINESS_UNIT_DIVISION', max_length=255, null=True)),
                ('GROUP_NAME', models.CharField(max_length=255, null=True)),
                ('GROUP_NAME1', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'stg_CLR_upload',
            },
        ),
        migrations.DeleteModel(
            name='CLRNew',
        ),
    ]
