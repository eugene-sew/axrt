from operator import index
from flask import Blueprint
from E_voting. models import User, Voterscount
from flask import flash, redirect, render_template, request, url_for, request
from flask_login import login_user, logout_user, current_user, login_required



admin_panel = Blueprint('admin_panel', __name__)



@admin_panel.route('/adminonlyHTU@2120/<int:post_id>', methods=['GET', 'POST'])
@login_required
def masterpage(post_id):
    user = current_user
    members = User.query.all()
    return render_template('masterpage.html', user=user, members=members, post_id=post_id)



@admin_panel.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out successfuly', category='success')
    return redirect(url_for('views.home'))
    return render_template('home.html')
