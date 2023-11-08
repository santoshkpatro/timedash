class TimedashDBRouter:
    TRANSACTION_MODELS = ['order', 'payment']

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        match db:
            case 'default':
                return model_name not in self.TRANSACTION_MODELS
            case 'main':
                return model_name in self.TRANSACTION_MODELS
            case 'sandbox':
                return model_name in self.TRANSACTION_MODELS