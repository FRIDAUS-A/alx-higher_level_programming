$(document).ready(() => {
	const urlApi = "https://swapi-api.alx-tools.com/api/films/?format=json";
	$.ajax({
		url: urlApi,
		method: 'GET',
		dataType: 'json',
		success: (data) => {
			let listData = JSON.stringify(data.results)
			listData = JSON.parse(listData)
			console.log(listData)
			for (let count = 0; count < listData.length; count++){
				title = '<li>' + listData[count].title + '</li>'
				$('ul#list_movies').append(title)
			}
		}
	})
})