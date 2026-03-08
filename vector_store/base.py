class VectorStore:
    def add(self,texts,vectors):
        raise NotImplementedError
    
    def search(Self,query_vector,top_k):
        raise NotImplementedError
    