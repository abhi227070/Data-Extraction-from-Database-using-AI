from langchain_experimental.sql import SQLDatabaseChain
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX,_mysql_prompt
from langchain.prompts.prompt import PromptTemplate
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.prompts import FewShotPromptTemplate
from data.few_shots_data import few_shots

def new_chain_connection(llm,db):
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    to_vectorize = [" ".join(example.values()) for example in few_shots]
    vectordatabase = Chroma.from_texts(to_vectorize,embedding=embeddings,metadatas=few_shots)

    example_templet = PromptTemplate(
        input_variables = ["Question","SQLQuery","SQLResult","Answer"],
        template = "\nQuestion: {Question} \nSQLQuery: {SQLQuery} \nSQLResult: {SQLResult} \nAnswer: {Answer}"
    )

    example_selector = SemanticSimilarityExampleSelector(
        vectorstore = vectordatabase,
        k = 2
    )

    few_shot_prompt = FewShotPromptTemplate(
        example_selector = example_selector,
        example_prompt = example_templet,
        prefix = _mysql_prompt,
        suffix = PROMPT_SUFFIX,
        input_variables = ["input","table_info","top_k"]
    )

    new_chain = SQLDatabaseChain.from_llm(llm,db,verbose=True, prompt = few_shot_prompt,return_intermediate_steps=True)
    
    return new_chain