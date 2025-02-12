import  requests
import _datetime as dt

pixela_post_endpoint = "https://pixe.la/v1/users"
today = dt.datetime.now()
today_str = today.strftime("%Y%m%d")
link = "https://pixe.la/v1/users/atish14/graphs/graph2.html"

option = int(input("Please the required option please:\n1 for adding today's data\n2 for update\n3 for delete\n"))



#Creating a user account in pixela
parameters = {
    "token":"atish14191419",
    "username": "atish14",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
# response = requests.post(url= pixela_post_endpoint, json= parameters)
# print(response.text)



header = {
    "X-USER-TOKEN":"atish14191419",
}



#creating a graph about one of your habit in pixela
pixela_graph_post = "https://pixe.la/v1/users/atish14/graphs"
parameters_graph = {
    "id":"graph2",
    "name":"coding habit graph",
    "unit":"hour",
    "type":"float",
    "color":"sora",
}
# response_graph = requests.post(url=pixela_graph_post, json=parameters_graph,headers=header)
# print(response_graph.text)



if option == 1:
    amount = str(input("For how much hour did you learn coding today?\n"))
    pixela_pixel_endpoint ="https://pixe.la/v1/users/atish14/graphs/graph2"
    parameter_pixel = {
        "date": f"{today_str}",
        "quantity":f"{amount}",
    }
    response_add = requests.post(url=pixela_pixel_endpoint, json= parameter_pixel,headers=header)
    print(response_add.text)
    print(f"Check on this link: {link}")

elif option == 2:
    date = str(input("Please enter the date you want to update in YYYYMMDD format:\n"))
    value = str(input("Please enter the updated value:\n"))
    pixela_pixel_update_endpoint = f"https://pixe.la/v1/users/atish14/graphs/graph2/{date}"
    parameter_update_pixel ={
        "quantity":f"{value}",
    }
    response_update = requests.put(url=pixela_pixel_update_endpoint,json=parameter_update_pixel,headers=header)
    print(response_update.text)
    print(f"Check on this link: {link}")

elif option == 3:
    date = str(input("Please enter the date you want to delete in YYYYMMDD format:\n"))
    pixela_pixel_delete = f"https://pixe.la/v1/users/atish14/graphs/graph2/{date}"
    response = requests.delete(url= pixela_pixel_delete, headers= header)
    print(response.text)
    print(f"Check on this link: {link}")

else:
    print("Choose the correct option please!!")