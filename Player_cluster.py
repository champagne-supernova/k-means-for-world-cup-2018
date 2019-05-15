def cluster(player, result):
    player_cluster = []
    for i in range(len(player)):
        player_info = {}
        #  注意：这句话一定要放到循环里面！！！
        player_info['name'] = player[i][1]
        player_info['country'] = player[i][2]
        player_info['cluster'] = result[i]
        player_cluster.append(player_info)
    print(player_cluster)
    n = max(result)
    filename = 'forward.txt'

    for i in range(n+1):
        print("\n\ncluster"+str(i)+":\n")
        with open(filename, 'a') as file_object:
            file_object.write("cluster"+str(i)+":")

        for player in player_cluster:
            if player['cluster'] == i:
                print(player['name']+" "+player['country'])
                with open(filename, 'a') as file_object:
                    file_object.write(player['name']+" "+player['country']+'\n')
