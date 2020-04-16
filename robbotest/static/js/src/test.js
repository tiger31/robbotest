function TestXBlock(runtime, element) {
	const handlerUrl = runtime.handlerUrl(element, 'increment_count');
	element.children[0].setAttribute("url", handlerUrl)
}