import asyncio

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()


prompt = ChatPromptTemplate.from_messages([
    ("system", "Sos un asistente útil y claro."),
    ("human", "{pregunta}")
])


model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    temperature=0
)


chain = prompt | model | StrOutputParser()


async def main():
    respuesta = await chain.ainvoke({
        "pregunta": "¿Qué es LCEL en una frase?"
    })

    print(respuesta)


if __name__ == "__main__":
    asyncio.run(main())