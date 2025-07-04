from django.apps import AppConfig

class CrowdfundingCoreConfig(AppConfig): # Renamed class
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crowdfunding_core' # Renamed app identifier
    verbose_name = 'Crowdfunding Core Logic' # Anglicized verbose_name
