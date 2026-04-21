from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'clave-secreta-para-desarrollo')

# Formulario de contacto usando WTForms
class ContactForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Mensaje', validators=[DataRequired()])
    submit = SubmitField('Enviar mensaje')

# Datos de ejemplo para proyectos y habilidades
PROYECTOS = [
    {
        'titulo': 'E‑commerce de moda',
        'descripcion': 'Plataforma completa con carrito de compras y pasarela de pagos.',
        'tecnologias': ['Flask', 'Bootstrap', 'SQLite', 'PayPal API'],
        'imagen': 'https://picsum.photos/id/20/400/250'  # imagen de ejemplo
    },
    {
        'titulo': 'Panel de análisis de ventas',
        'descripcion': 'Dashboard interactivo con gráficos y exportación de datos.',
        'tecnologias': ['Flask', 'Chart.js', 'Pandas', 'Bulma'],
        'imagen': 'https://picsum.photos/id/24/400/250'
    },
    {
        'titulo': 'Blog de tecnología',
        'descripcion': 'Blog funcional con autenticación de usuarios y comentarios.',
        'tecnologias': ['Flask', 'SQLAlchemy', 'WTForms', 'Bootstrap'],
        'imagen': 'https://picsum.photos/id/26/400/250'
    }
]

HABILIDADES = [
    {'nombre': 'Python / Flask', 'nivel': '90%', 'icono': 'bi-file-code'},
    {'nombre': 'HTML5 & CSS3', 'nivel': '85%', 'icono': 'bi-braces'},
    {'nombre': 'JavaScript', 'nivel': '75%', 'icono': 'bi-browser-chrome'},
    {'nombre': 'Bootstrap 5', 'nivel': '80%', 'icono': 'bi-bootstrap'},
    {'nombre': 'SQL / SQLAlchemy', 'nivel': '70%', 'icono': 'bi-database'},
    {'nombre': 'Git & GitHub', 'nivel': '85%', 'icono': 'bi-github'}
]

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    if form.validate_on_submit():
        # Simulamos el envío del mensaje (solo mostramos un mensaje de éxito)
        # En producción podrías enviar un correo o guardar en base de datos
        flash(f'¡Gracias {form.name.data}! Tu mensaje ha sido enviado correctamente.', 'success')
        # Limpiar el formulario redirigiendo para evitar reenvío
        return redirect(url_for('index'))
    return render_template('index.html',
                           proyectos=PROYECTOS,
                           habilidades=HABILIDADES,
                           form=form)

if __name__ == '__main__':
    app.run(debug=True)