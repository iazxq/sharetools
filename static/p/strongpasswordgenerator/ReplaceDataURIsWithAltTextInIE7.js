/**
 * Created with PyCharm.
 * User: Administrator
 * Date: 13-8-18
 * Time: 上午10:16
 * To change this template use File | Settings | File Templates.
 */
var i, allImages = document.getElementsByTagName("img");	//gets all the image elements
for (i = 0; i < allImages.length;) {	//we'll be replacing an image element on each iteration, so there'll one fewer image element, so we don't need to increment the counter in this loop
	if (allImages[i].getAttribute("src").substring(0,10)==="data:image"){	//if this image element uses a dataURI
		allImages[i].parentNode.replaceChild(document.createElement("span").appendChild(document.createTextNode(allImages[i].getAttribute("alt"))), allImages[i]);	//put this image element's alt attribute into a text node, put that node into a span element, and replace this image element with the span element
	}
}
