$(document).ready(() => {
	const urlApi = "https://hellosalut.stefanbohacek.dev/?lang=fr ";
	$.ajax({
		url: urlApi,
		method: 'GET',
		dataType: 'json',
		success: (data) => {
			$('div#hello').html(JSON.stringify(data.hello))
		}
	})
})