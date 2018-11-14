from flask import Flask ,jsonify, request
app= Flask(__name__)
'''these are the datastructures holding our data for the representational state transfer'''
menu = [{'name': 'services offered Time of the Day'},{'name':'Breskfast 7-11:00am'},{'name':'Lunch 12-2:00pm'},{'name':'Dinner 4-11:00pm'}]
Lunch= [{'food':'matooke'},{'food':'rice'},{'food':'posho'},{'food':'kalo'}]
Breakfast= [{'Beverage':'coffee'},{'Beverage':'Tea'},{'Beverage':'Vanilla'},{'Beverage':'Porridge'},]
Dinner= [{'food':'matooke & beans'},{'food':'rice $ tuna'},{'food':'posho $ meketu '},{'food':'kalo $ qwerty'}]

matooke=[{'details':'Quantiy-2pnds,source-meat,temp-hot'}]
rice=[{'details':'Quantiy-1pnds,source-meat,gnutpaste,temp-hot'}]
kalo=[{'details':'Quantiy-2.5pnds,source-meat,beans,temp-hot'}]
posho=[{'details':'Quantiy-0.5pnds,source-meat,temp-hot'}]

'''this endpoint welcomes the customers '''
@app.route("/",methods=['GET'])
def index():
	return jsonify({'Message':'youre welcome'})

'''this endpoint shows all the services offered'''
@app.route("/services", methods=['GET'])
def services():
	return jsonify({'menu':menu})


'''this endpoint shows all the services specified by the name in the route'''
@app.route("/services/<string:name>" ,methods=['GET'])
def name_of_the_service(name):
	men =[service for service in menu if service['name'] == name ] 
	return jsonify({'service':men[0]})
	

'''this endpoint shows all the lunch packages offered by the restaurant'''
@app.route("/services/lunchdetails" ,methods=['GET'])
def name_of_the_service_and_list_of_foods():
	return jsonify({'Lunch':Lunch})

'''this endpoint shows all the specific lunch packages offered by the restaurant as specified by the customers'''
@app.route("/services/lunchdetails/<string:food>" ,methods=['GET'])
def name_of_the_lunchfoods(food):
	lunchfood= [ meal for meal in Lunch if meal['food']==food]
	return jsonify({'Lunchtime meal':lunchfood[0]})


'''this endpoint shows all the breakfast packages offered by the restaurant'''
@app.route("/services/breakfastdetails" ,methods=['GET'])
def name_of_the_service_and_list_of_breakfastfoods():
	return jsonify({'Breakfast':Breakfast})

'''this endpoint shows all the specific breakfast packages offered by the restaurant as specified by the customers'''
@app.route("/services/breakfastdetails/<string:Beverage>" ,methods=['GET'])
def name_of_the_breakfastfoods(Beverage):
	bfastfoods= [ meal for meal in Breakfast if meal['Beverage']==Beverage]
	return jsonify({'Braskfast meal':bfastfoods[0]})

'''this endpoint shows all the matooke packages in details as offered by the restaurant'''
@app.route('/food/details/matooke')
def details():
	return jsonify({'matooke meal has the following': matooke})

'''this endpoint shows all the rice packages  in details as offered by the restaurant'''
@app.route('/food/details/rice')
def ricedetails():
	return jsonify({'rice meal has the following': rice})

'''this endpoint shows all the posho packages  in details as offered by the restaurant'''
@app.route('/food/details/posho')
def poshoetails():
	return jsonify({'posho meal has the following': posho})


'''this endpoint shows all the kalo packages  in details as offered by the restaurant'''
@app.route('/food/details/kalo')
def kalodetails():
	return jsonify({'kalo meal has the following': kalo})

'''this endpoint adds more services offered by the restaurant'''
@app.route("/services", methods=['POST'])
def addingservices():
	add = {'name':request.json['name']}
	menu.append(add)
	return jsonify({'Message':'successfully added'})

'''this endpoint adds more details on the lunch-services offered by the restaurant'''	
@app.route("/services/lunchdetails" ,methods=['POST'])
def Adding_more_to_list_of_foods():
	item_to_add= {'food':request.json['food']}
	Lunch.append(item_to_add)
	return jsonify({'Message':'food item added to lunch menu'})

'''this endpoint adds more details on the breakfast-services offered by the restaurant'''	
@app.route("/services/breakfastdetails" ,methods=['POST'])
def Adding_more_to_list_of_foods_breakfast():
	item_to_add= {'Beverage':request.json['Beverage']}
	Breakfast.append(item_to_add)
	return jsonify({'Message':'food item added to breakfast menu'})


'''this endpoint adds more details on the matooke offered by the restaurant'''	
@app.route('/food/details/matooke',methods=['POST'])
def adding_matooke_details():
	matoke={'details':request.json['details']}
	matooke.append(matoke)
	return jsonify({'Message': 'More details have been attached to the matooke details'})


'''this endpoint adds more details on the rice offered by the restaurant'''	
@app.route('/food/details/rice',methods=['POST'])
def adding_rice_details():
	Rice= {'details':request.json['details']}
	rice.append(Rice)
	return jsonify({'Message': 'rice meal details added successfully'})


'''this endpoint adds more details on the posho offered by the restaurant'''	
@app.route('/food/details/posho', methods=['POST'])
def adding_poshoetails():
	posh={'details':request.json['details']}
	posho.append(posh)
	return jsonify({'Message': 'posh meal details added successfully'})


'''this endpoint adds more details on the lunch-services offered by the restaurant'''	
@app.route('/food/details/kalo',methods=['POST'])
def adding_kalodetails():
	kal={'details':request.json['details']}
	kalo.append(kal)
	return jsonify({'Message': 'kalo meal details added successfully'})

'''this endpoint modifies services offered by the restaurant'''	
@app.route("/services/<string:name>" ,methods=['PUT'])
def changing_the_name_of_the_service(name):
	men =[service for service in menu if service['name'] == name ] 
	men[0]['name']=request.json['name']
	return jsonify({'Message':'thank you , successfully changed '})


'''this endpoint modifies details of the lunch services offered by the restaurant'''	
@app.route("/services/lunchdetails/<string:food>" ,methods=['PUT'])
def changing_the_name_of_the_lunchfoods(food):
	lunchfood= [ meal for meal in Lunch if meal['food']==food]
	lunchfood[0]['food']=request.json['food']
	return jsonify({'Message':'thank you , successfully changed '})
	
'''this endpoint modifies details of the breakfast services offered by the restaurant'''	
@app.route("/services/breakfastdetails/<string:Beverage>" ,methods=['PUT'])
def changing_the_name_of_the_breakfastfoods(Beverage):
	bfastfoods= [ meal for meal in Breakfast if meal['Beverage']==Beverage]
	bfastfoods[0]['Beverage']=request.json['Beverage']

'''this endpoint deletes services offered by the restaurant'''	
@app.route("/services/<string:name>" ,methods=['DELETE'])
def deleting_the_name_of_the_service(name):
	men =[service for service in menu if service['name'] == name ] 
	menu.remove(men[0])
	return jsonify({'Message':'thank you , successfully deleted '})

'''this endpoint deletes a lunch specific food offered by the restaurant'''	
@app.route("/services/lunchdetails/<string:food>" ,methods=['DELETE'])
def deletinging_the_name_of_the_lunchfoods(food):
	lunchfood= [ meal for meal in Lunch if meal['food']==food]
	Lunch.remove(lunchfood[0])
	return jsonify({'Message':'thank you , successfully deleted '})
	

'''this endpoint deletes a breakfast specific Beverage offered by the restaurant'''	
@app.route("/services/breakfastdetails/<string:Beverage>" ,methods=['DELETE'])
def deleting_the_name_of_the_breakfastfoods(Beverage):
	bfastfoods= [ meal for meal in Breakfast if meal['Beverage']==Beverage]
	Brealfast.remove(bfastfoods[0])

if __name__ == "__main__":
	app.run(debug=True)
