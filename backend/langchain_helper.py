# Importing all the dependencies or folders
from src.database_connection import database_connection
from src.llm_connection import llm_connection
from src.new_chain_connection import new_chain_connection



# Class to create required model using Langchain and run
class get_langchain_output:
    
    def __init__(self) -> None:
        llm = llm_connection()
        db = database_connection()
        self.new_chain = new_chain_connection(llm=llm,db=db)
        
    def run(self,question):
        
        try:
            answer = self.new_chain.invoke(question)
            return answer
        except Exception as exc:
            return "Oops.. Some Error Occour."
        