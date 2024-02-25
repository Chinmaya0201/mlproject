from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

from src.pipeline.predict_pipeline import CustomData, PredictPipeline


app = FastAPI()

templates = Jinja2Templates('templates')

# @app.get("/", response_class= HTMLResponse)
# def index(request: Request):

#     context = {'request':request}

#     return templates.TemplateResponse("index.html", context= context)

# @app.add_route('/predictdata', methods= ['GET', 'POST'], response_class= HTMLResponse)
# def predict_datapoint(request: Request):

#     context = {'request':request}

#     if request.method == 'GET':

#         return templates.TemplateResponse('index.html', context= context)

@app.get('/', response_class= HTMLResponse)
def predict_datapoint(request: Request):
    
    context = {'request':request}

    return templates.TemplateResponse('home.html', context= context)

@app.post('/', response_class= HTMLResponse)
async def predict_datapoint(request: Request):
    
    form_data = await request.form()

    # gender = form_data['gender']
    # print(gender)
    
    data = CustomData(
            gender=form_data['gender'],
            race_ethnicity=form_data['ethnicity'],
            parental_level_of_education=form_data['parental_level_of_education'],
            lunch=form_data['lunch'],
            test_preparation_course=form_data['test_preparation_course'],
            reading_score=float(form_data['writing_score']),
            writing_score=float(form_data['reading_score'])
        )
    
    pred_df=data.get_data_as_data_frame()

    predict_pipeline=PredictPipeline()
    results=predict_pipeline.predict(pred_df)
    
    # context = {'request':request,
    #            'results':'fuck yes'}

    context = {'request': request,
               "results": results[0]}

    return templates.TemplateResponse('home.html', context= context)

if __name__ == '__main__':

    uvicorn.run("app_v2:app", reload= True)