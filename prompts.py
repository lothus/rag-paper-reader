from langchain_community.document_loaders import PyPDFLoader


class Prompts:
    '''
    Control all the prompt creattion for the calls
    '''

    def __init__(self) -> None:
        self.system_message = "Return the key points in 3 paragprah or less from the document"
        
        

    def load_pdf(self,file_paths:list) -> None:
        self.reference_file = PyPDFLoader(file_paths)
        