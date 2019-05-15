import data_initialize as di
import find_k
import Player_cluster

sheet_name = '门将'
player = di.load_data(sheet_name)
player = di.process_data(player)
print(player)
player_features = di.normalize_data(player)
result = find_k.find_the_best_k(player_features)
Player_cluster.cluster(player, result)
