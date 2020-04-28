function TestXBlockEditor(runtime, element) {
	const handlerUrl = runtime.handlerUrl(element, 'studio_submit');
	$(element).children().attr("url", handlerUrl)
}