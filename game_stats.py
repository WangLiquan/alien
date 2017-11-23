from settings import Settings
import os

class GameStats(): 
	"""跟踪游戏的统计信息"""
	def __init__(self, ai_settings):
		super(GameStats, self).__init__()
		self.ai_settings = ai_settings
		self.reset_stats()
		if os.path.exists(ai_settings.high_score_fileName):
			with open(ai_settings.high_score_fileName) as file_object:
				self.high_score = int(file_object.read()) 
		else:
			self.high_score = 0

		# 游戏刚启动时处于活动状态
		self.game_active = False

	def reset_stats(self):
		"""初始化在游戏运行期间可能变化的统计信息"""
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1
