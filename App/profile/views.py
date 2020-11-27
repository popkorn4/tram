from . import profile
from flask import render_template, redirect, session, url_for, g, flash, request
from .models import categories, tablet, orders
from .forms import AddProduct, login, order
from cloudipsp import Api, Checkout
@profile.route('/')
def about():
    return render_template("f.html")
@profile.route('/category/<string:name>')
def cayegory(name):
    products = tablet.objects(category = name)
    print(products)
    return render_template("Теннис.html",m=products, c=name)
@profile.route('/buy/<int:id>')
def buy(id):
    produkt=tablet.objects(Tablet_Id=id).first()
    return render_template("gg.html",lll=produkt)
@profile.route('/add_product/', methods = ['GET', 'POST'])#methods = ['GET', 'POST']-пишется когда есть форма(для заполнения)
def add_product():
    if 'login' not in session:
        return redirect(url_for('profile.about'))
    form = AddProduct() #создаём переменную form, типа AddProduct
    if form.validate_on_submit():#проверка что пользователь нажал на кнопку
        # if form.price.data is None:
        #     flash('Неправилтно ввели цену', 'error')
        #     return redirect(url_for('profile.add_product'))
        if categories.objects(name = form.category.data):
            print('такая котегория уже есть')
        else:
            categ = categories(
                                name = form.category.data,
                                )
            categ.save()#Создаём новую категорию еси её не было

        item = tablet(
                    Name = form.name.data,
                    category = form.category.data,
                    About = form.description.data,
                    picture = form.photo_hash.data,
                    price = form.price.data
                    )
        item.save()#Создаём новый товар
        flash('Всё хорошо', 'error')
    return render_template("admin.html", form = form)
@profile.route("/admin/", methods = ['GET', 'POST'])#methods = ['GET', 'POST']-пишется когда есть форма(для заполнения)
def admin():
    form = login() #создаём переменную form, типа login
    if form.validate_on_submit():#проверка что пользователь нажал на кнопку
        if form.login.data == '12345':
            session['login'] = True
            return redirect(url_for('profile.add_product'))
        else:
            return redirect(url_for('profile.about'))
    return render_template("login.html", form = form)
@profile.route('/logout/')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/')
@profile.route('/real_buy/<int:id>')
def real_buy(id):
    product=tablet.objects(Tablet_Id=id).first()
    api = Api(merchant_id=1396424,
          secret_key='test')
    checkout = Checkout(api=api)
    data = {
        "currency": "EUR",
        "amount": product.price+"00"
    }
    url = checkout.url(data).get('checkout_url')
    return redirect(url)
@profile.route('/orders/', methods = ['GET', 'POST'])
def Orders():
    orders_form = order()
    item_list = []
    # session['items'] = ''
    items = []
    if 'items' in session:#проверяем есть ли товары в session
        dat = session['items'].split() #Забераем товары из session
        for it_id in dat:
            items.append(tablet.objects(Tablet_Id = it_id).first())#items-массив с полной информацией о товарах,затем мы передадим массив в html

    if orders_form.validate_on_submit():
        if 'items' in session:
            dat = session['items'].split()
            for item_id in dat:
                item = tablet.objects(Tablet_Id = item_id).first()
                item_list.append(item)
            order1 = orders(
                            Name = orders_form.Name.data, 
                            adress = orders_form.adress.data,
                            tel = orders_form.tel.data,
                            tablets_id = item_list
                          )
            order1.save()
            session['items'] = ''

    return render_template("корзина.html", items = items, form = orders_form)
@profile.route('/add_item_in_order/', methods = ['POST'])
def add_in_order():
    data = request.form['id']

    if 'items' in session:
        session['items'] += (data+' ')
    else:
        session['items'] = data
    return('success')