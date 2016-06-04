from django_assets import Bundle, register
js = Bundle('js/vendor/jquery-2.1.1.min.js', 'js/vendor/modernizr-2.8.3-respond-1.4.2.min.js', 'js/vendor/materialize.min.js', 'js/main.js', filters='jsmin', output='js/main.min.js')
register('js_all', js)
css = Bundle('css/vendor/normalize.min.css', 'css/main.css', filters='cssmin', output='css/main.min.css')
register('css_all', css)
