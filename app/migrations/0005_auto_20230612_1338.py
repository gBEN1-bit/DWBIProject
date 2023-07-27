# Generated by Django 2.2.28 on 2023-06-12 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20230612_1311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clr',
            old_name='br',
            new_name='BR',
        ),
        migrations.RenameField(
            model_name='clr',
            old_name='collateral_desc',
            new_name='COLLATERAL_DESC',
        ),
        migrations.RenameField(
            model_name='clr',
            old_name='collateral_type',
            new_name='COLLATERAL_TYPE',
        ),
        migrations.RenameField(
            model_name='clr',
            old_name='age_of_unpaid_obligation_days',
            new_name='INSTALLMENT',
        ),
        migrations.RenameField(
            model_name='clr',
            old_name='approved_amount_original_ccy',
            new_name='INT_RATE',
        ),
        migrations.RenameField(
            model_name='clr',
            old_name='approved_amount_usd',
            new_name='LAST_3MONTH_CREDIT',
        ),
        migrations.RenameField(
            model_name='clr',
            old_name='business_unit_division',
            new_name='REF_NO',
        ),
        migrations.RenameField(
            model_name='clr',
            old_name='collateral_value_usd',
            new_name='SECTOR',
        ),
        migrations.RenameField(
            model_name='clr',
            old_name='cap_era_interest_rates',
            new_name='SETTLEMENT_ACCOUNT',
        ),
        migrations.RenameField(
            model_name='clr',
            old_name='cbk_grade',
            new_name='TENOR',
        ),
        migrations.RenameField(
            model_name='clr',
            old_name='collateral_value_kes',
            new_name='UNPAID_INSTALLMENT',
        ),
        migrations.RenameField(
            model_name='clr',
            old_name='date_of_last_credit',
            new_name='VALUE_DATE',
        ),
        migrations.RemoveField(
            model_name='clr',
            name='current_exposure_original_ccy',
        ),
        migrations.RemoveField(
            model_name='clr',
            name='current_exposure_usd',
        ),
        migrations.RemoveField(
            model_name='clr',
            name='impairment_usd',
        ),
        migrations.RemoveField(
            model_name='clr',
            name='installment',
        ),
        migrations.RemoveField(
            model_name='clr',
            name='int_rate',
        ),
        migrations.RemoveField(
            model_name='clr',
            name='last_3month_credit',
        ),
        migrations.RemoveField(
            model_name='clr',
            name='last_credit_amount',
        ),
        migrations.RemoveField(
            model_name='clr',
            name='one_month_collection',
        ),
        migrations.RemoveField(
            model_name='clr',
            name='outstanding_balance_usd',
        ),
        migrations.RemoveField(
            model_name='clr',
            name='ref_no',
        ),
        migrations.RemoveField(
            model_name='clr',
            name='sector',
        ),
        migrations.RemoveField(
            model_name='clr',
            name='settlement_account',
        ),
        migrations.RemoveField(
            model_name='clr',
            name='sn',
        ),
        migrations.RemoveField(
            model_name='clr',
            name='tenor',
        ),
        migrations.RemoveField(
            model_name='clr',
            name='three_months_collections',
        ),
        migrations.RemoveField(
            model_name='clr',
            name='unpaid_amount_ghc_missed',
        ),
        migrations.RemoveField(
            model_name='clr',
            name='unpaid_amount_usd',
        ),
        migrations.RemoveField(
            model_name='clr',
            name='unpaid_installment',
        ),
        migrations.RemoveField(
            model_name='clr',
            name='value_date',
        ),
        migrations.AddField(
            model_name='clr',
            name='AGE_OF_UNPAID_OBLIGATION_DAYS',
            field=models.FloatField(db_column='AGE OF UNPAID OBLIGATION (DAYS)', null=True),
        ),
        migrations.AddField(
            model_name='clr',
            name='APPROVED_AMOUNT_ORIGINAL_CCY',
            field=models.FloatField(db_column='APPROVED AMOUNT (ORIGINAL CCY)', null=True),
        ),
        migrations.AddField(
            model_name='clr',
            name='APPROVED_AMOUNT_USD',
            field=models.FloatField(db_column='APPROVED AMOUNT (USD)', null=True),
        ),
        migrations.AddField(
            model_name='clr',
            name='BUSINESS_UNIT_DIVISION',
            field=models.CharField(db_column='BUSINESS UNIT / DIVISION', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='clr',
            name='CAP_ERA_INTEREST_RATES',
            field=models.CharField(db_column='Cap era(INTEREST RATES)', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='clr',
            name='CBK_GRADE',
            field=models.FloatField(db_column='CBK GRADE', null=True),
        ),
        migrations.AddField(
            model_name='clr',
            name='COLLATERAL_VALUE_KES',
            field=models.FloatField(db_column='COLLATERAL_VALUE (kes)', null=True),
        ),
        migrations.AddField(
            model_name='clr',
            name='COLLATERAL_VALUE_USD',
            field=models.CharField(db_column='COLLATERAL_VALUE (USD)', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='clr',
            name='CURRENT_EXPOSURE_ORIGINAL_CCY',
            field=models.FloatField(db_column='CURRENT EXPOSURE (ORIGINAL CCY)', null=True),
        ),
        migrations.AddField(
            model_name='clr',
            name='CURRENT_EXPOSURE_USD',
            field=models.FloatField(db_column='CURRENT EXPOSURE (USD)', null=True),
        ),
        migrations.AddField(
            model_name='clr',
            name='DATE_OF_LAST_CREDIT',
            field=models.DateTimeField(db_column='DATE OF LAST CREDIT', null=True),
        ),
        migrations.AddField(
            model_name='clr',
            name='IMPAIRMENT_USD',
            field=models.FloatField(db_column='IMPAIRMENT -USD', null=True),
        ),
        migrations.AddField(
            model_name='clr',
            name='LAST_CREDIT_AMOUNT',
            field=models.FloatField(db_column='LAST CREDIT AMOUNT', null=True),
        ),
        migrations.AddField(
            model_name='clr',
            name='ONE_MONTH_COLLECTION',
            field=models.FloatField(db_column='1 MONTH COLLECTION', null=True),
        ),
        migrations.AddField(
            model_name='clr',
            name='OUTSTANDING_BALANCE_USD',
            field=models.FloatField(db_column='OUTSTANDING BALANCE (USD)', null=True),
        ),
        migrations.AddField(
            model_name='clr',
            name='S_N',
            field=models.FloatField(db_column='S/N', null=True),
        ),
        migrations.AddField(
            model_name='clr',
            name='THREE_MONTHS_COLLECTIONS',
            field=models.CharField(db_column='3-MONTHS COLLECTIONS', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='clr',
            name='UNPAID_AMOUNT_GHC_MISSED',
            field=models.FloatField(db_column='UNPAID AMOUNT (GHC)- MISSED', null=True),
        ),
        migrations.AddField(
            model_name='clr',
            name='UNPAID_AMOUNT_USD',
            field=models.FloatField(db_column='UNPAID AMOUNT (USD)', null=True),
        ),
    ]
