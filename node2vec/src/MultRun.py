'''
Reference implementation of node2vec. 

Author: Aditya Grover

For more details, refer to the paper:
node2vec: Scalable Feature Learning for Networks
Aditya Grover and Jure Leskovec 
Knowledge Discovery and Data Mining (KDD), 2016
'''

import argparse
import numpy as np
import networkx as nx
import node2vec
from gensim.models import Word2Vec

def parse_args():
	'''
	Parses the node2vec arguments.
	'''
	parser = argparse.ArgumentParser(description="Run node2vec.")

	parser.add_argument('--input', nargs='?', default='graph/Slashdot_Data_For_Embedding_unweight_1.txt',
	                    help='Input graph path')

	parser.add_argument('--output', nargs='?', default='emb/Slashdot_Embedding_Result_1.txt',
	                    help='Embeddings path')

	parser.add_argument('--dimensions', type=int, default=100,
	                    help='Number of dimensions. Default is 128.')

	parser.add_argument('--walk-length', type=int, default=10,
	                    help='Length of walk per source. Default is 80.')

	parser.add_argument('--num-walks', type=int, default=1,
	                    help='Number of walks per source. Default is 10.')

	parser.add_argument('--window-size', type=int, default=3,
                    	help='Context size for optimization. Default is 10.')

	parser.add_argument('--iter', default=5, type=int,
                      help='Number of epochs in SGD')

	parser.add_argument('--workers', type=int, default=8,
	                    help='Number of parallel workers. Default is 8.')

	parser.add_argument('--p', type=float, default=1,
	                    help='Return hyperparameter. Default is 1.')

	parser.add_argument('--q', type=float, default=1,
	                    help='Inout hyperparameter. Default is 1.')

	parser.add_argument('--weighted', dest='weighted', action='store_true',
	                    help='Boolean specifying (un)weighted. Default is unweighted.')
	parser.add_argument('--unweighted', dest='unweighted', action='store_false')
	parser.set_defaults(weighted=False)

	parser.add_argument('--directed', dest='directed', action='store_true',
	                    help='Graph is (un)directed. Default is undirected.')
	parser.add_argument('--undirected', dest='undirected', action='store_false')
	parser.set_defaults(directed=True)

	return parser.parse_args()

def read_graph(unweight_path):
	'''
	Reads the input network in networkx.
	'''
	if args.weighted:
		G = nx.read_edgelist(unweight_path, nodetype=int, data=(('weight',float),), create_using=nx.DiGraph())
	else:
		G = nx.read_edgelist(unweight_path, nodetype=int, create_using=nx.DiGraph())
		for edge in G.edges():
			G[edge[0]][edge[1]]['weight'] = 1

	if not args.directed:
		G = G.to_undirected()

	return G

def learn_embeddings(walks,dim,win_size,t,Dataid):
	'''
	Learn embeddings by optimizing the Skipgram objective using SGD.
	'''
	walks = [map(str, walk) for walk in walks]
	model = Word2Vec(walks, size=dim, window=win_size, min_count=0, sg=1, workers=args.workers, iter=t)
	output_str='Slashdot090216_Embedding_Result10_'+str(Dataid)+'.txt'
	model.wv.save_word2vec_format(output_str)
	
	return

def main(args):
	'''
	Pipeline for representational learning for all nodes in a graph.
	'''
	num_walks = 3  # 5
	walk_length = 5  # 20
	dimensions = 100  # 100
	windows_size = 1  # 3
	iter = 5

	Data_Dict = {'digg': {'digg_meta': 'out.digg-friends', 'num': 3}
		, '': ''}
	dataname = 'digg'
	for Data_id in range(1):
		inputstr = '../../' + dataname + '/com/G_link_' + str(i) + '.txt'
		unweight_path = 'DataForEm/Slashdot090216_Data_For_Embedding_unweight_' + str(Data_id) + '.txt'
		# unweight_path = str(Data_id) + '/Slashot_Data_For_Embedding_unweight_' + str(Data_id) + '.txt'
		nx_G = read_graph(unweight_path)
		G = node2vec.Graph(nx_G, args.directed, args.p, args.q)
		G.preprocess_transition_probs()
		walks = G.simulate_walks(num_walks, walk_length)
		learn_embeddings(walks,dimensions,windows_size,iter,Data_id)

if __name__ == "__main__":
	args = parse_args()
	main(args)
