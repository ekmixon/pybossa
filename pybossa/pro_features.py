# -*- coding: utf8 -*-
# This file is part of PYBOSSA.
#
# Copyright (C) 2015 Scifabric LTD.
#
# PYBOSSA is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PYBOSSA is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PYBOSSA.  If not, see <http://www.gnu.org/licenses/>.


class ProFeatureHandler(object):

    def __init__(self, config):
        self.config = config

    def auditlog_enabled_for(self, user):
        return (
            user.is_authenticated and (user.admin or user.pro)
            if self.config.get('auditlog')
            else True
        )

    def webhooks_enabled_for(self, user):
        return (
            user.is_authenticated and (user.admin or user.pro)
            if self.config.get('webhooks')
            else True
        )

    def autoimporter_enabled_for(self, user):
        return (
            user.is_authenticated and (user.admin or user.pro)
            if self.config.get('autoimporter')
            else True
        )

    def better_stats_enabled_for(self, user, owner):
        return (
            owner.pro or user.is_authenticated and user.admin
            if self.config.get('better_stats')
            else True
        )

    def only_for_pro(self, feature):
        return self.config.get(feature)
