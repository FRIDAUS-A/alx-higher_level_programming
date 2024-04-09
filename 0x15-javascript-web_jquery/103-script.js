$(document).ready(() => {
	$('input#btn_translate').click(() => {
		translateHello();
	});
	$('#language_code').keypress((event) => {
        if (event.which === 13) {
            translateHello();
        }
    });
	function translateHello() {
		const languageCode = $('input#language_code').val().trim();
	const urlApi = `https://hellosalut.stefanbohacek.dev?lang=${languageCode}`;
	$.ajax({
		url: urlApi,
			method: 'GET',
			dataType: 'json',
			success: (data) => {
				const hello = data.hello
				$('div#hello').html(hello)
			}
	})
	}
});