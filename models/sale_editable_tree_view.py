# -*- coding: utf-8 -*-
from openerp.models import Model
from openerp.fields import Char


class sale_editable_tree_view(Model):
    _name = "sale_editable_tree_view.sale_editable_tree_view"

    name = Char()
