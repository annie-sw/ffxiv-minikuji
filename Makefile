all:
	rm -rf external
	mkdir -p external
	curl http://requirejs.org/docs/release/2.3.2/minified/require.js > external/require.js
	python PythonJS/pythonjs/translator.py --no-wrapper src/libminikuji.py > src/libminikuji.js
	curl -X POST -s --data-urlencode 'input@src/libminikuji.js' https://javascript-minifier.com/raw > libminikuji.min.js
