class GameStats():
    """Отслеживание статистики для игры Fire Tank"""
    
    def __init__(self, ai_settings):
        """Инициирует статистику"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Игра запускается в неактивном состоянии
        self.game_active = False
        
    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры"""
        self.lives_limit = self.ai_settings.lives_available
