# -*- coding: utf-8 -*-

#    Copyright (C) 2017-2018 Mathew Topper
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pytest

import random

import numpy as np
import pandas as pd

from dtocean_logistics.phases.operations import LogOp, logOp_init


@pytest.fixture(scope="module")
def op_db():

    x = {u'Logitic operation [-]': {u'Access': u'Access to the element',
                                    u'AssPort': u'Assembly at port',
                                    u'BurialToolDeploy':
                                        u'Deploy of Cable Burial Tool',
                                    u'BurialToolRecov':
                                        u'Recover cable burial tool',
                                    u'CableLay_Burial':
                                        (u'Cable lay and burial through cable '
                                         'route'),
                                    u'CableLay_Dyn':
                                        u'Cable lay with buoyancy modules',
                                    u'CableLay_Route':
                                        u'Cable lay through cable route',
                                    u'CableLay_SplitPipe':
                                        u'Cable lay with split pipes',
                                    u'CableLay_Trench':
                                        u'Cable lay through open trench',
                                    u'CaissonSuct':
                                        (u'Lowering anchors with mooring '
                                         'lines + Suction caisson anchor '
                                         'seafloor penetration + Tensioning'),
                                    u'ConnectPile':
                                        (u'Lowering mooring lines + '
                                         'Connecting end of mooring line to '
                                         'pre-installed pile + Tensioning'),
                                    u'Connect_Topside':
                                        (u'Connect top-side platform to the '
                                         'support structure'),
                                    u'DeckTrans': u'Deck transportation',
                                    u'Demob': u'Demobilisation',
                                    u'DevAssPort': u'Device assembly at port',
                                    u'DirecJet':
                                        (u'Lowering anchors with mooring '
                                         'lines + Direct-embedment anchor '
                                         'seafloor penetration through '
                                         'jetting-embedment + Tensioning'),
                                    u'DirecMech':
                                        (u'Lowering anchors with mooring '
                                         'lines + Direct-embedment anchor '
                                         'seafloor penetration through '
                                         'mechanical-embedment + Tensioning'),
                                    u'DirecSuct':
                                        (u'Lowering anchors with mooring '
                                         'lines + Direct-embedment anchor '
                                         'seafloor penetration through '
                                         'suction-embedment + Tensioning'),
                                    u'DragEmbed': 
                                        (u'Lowering mooring lines + '
                                         'Drag-embedment anchor seafloor '
                                         'penetration + Tensioning'),
                                    u'Dry_Connect':
                                        u'Conduct dry-mate connection on deck',
                                    u'GBSlow':
                                        (u'Gravity based foundation or anchor '
                                         'lowering'),
                                    u'GBSpos':
                                        (u'Gravity based foundation or anchor '
                                         'positioning'),
                                    u'Grout': u'Grouting',
                                    u'GroutRemov':
                                        u'Grouting equipment removal',
                                    u'HDD':
                                        (u'Vessel positioning + Connection to '
                                         'cable pull-head + Cable float-out + '
                                         'Cable pull-in through HDD conduit'),
                                    u'Install_mattress':
                                        (u'Lift and overboard concrete '
                                         'mattress + Lower concrete mattress '
                                         'to seabed + Position and release '
                                         'concrete mattress + Recover '
                                         'installation frame'),
                                    u'Install_rockbag':
                                        (u'Lift and overboard rock filter bag '
                                         '+ Lower rock filter bag to seabed + '
                                         'Position and release concrete '
                                         'mattress'),
                                    u'Jtube_Connect':
                                        (u'J-tube entrance inspection + Guide '
                                         'wire connection + Cable lay + Cable '
                                         'pull + Cable connection'),
                                    u'Lift_Cable_Seabed':
                                        u'Lift cable-end from seabed',
                                    u'Lift_Topside': u'Lift top-side platform',
                                    u'LoadCableFactory':
                                        u'Loading cable from factory port',
                                    u'LoadOut_Float':
                                        u'Load-out: Floated Away',
                                    u'LoadOut_Lift': u'Load-out:Lifted away',
                                    u'LoadOut_Skidded':
                                        u'Load-out:Skidded/Trailler',
                                    u'Lower_CP_Seabed':
                                        (u'Lower collection point to the '
                                         'seabed'),
                                    u'Lower_Cable_Seabed':
                                        u'Lower cable-end to the seabed',
                                    u'Maintenance':
                                        (u'Inspection or Maintenance '
                                         'Operations'),
                                    u'Mob': u'Mobilisation',
                                    u'OCT':
                                        (u'Vessel Positioning + Connection to '
                                         'cable pull-head + Cable float-out + '
                                         'Cable lay into pre-excavated '
                                         'trench'),
                                    u'PileDrill':
                                        (u'Driven pile foundation or anchor '
                                         'seafloor penetration through '
                                         'drilling rig + positioning'),
                                    u'PileHamm':
                                        (u'Driven pile foundation or anchor '
                                         'seafloor penetration through '
                                         'hammering + positioning'),
                                    u'PileVibro':
                                        (u'Driven pile foundation or anchor '
                                         'seafloor penetration through '
                                         'vibro-driving + positioning'),
                                    u'PosBFdev':
                                        (u'On-site posisitioning and '
                                         'connection of bottom-fixed device'),
                                    u'PosFLTdev':
                                        (u'On-site posisitioning and '
                                         'connection of floating device'),
                                    u'Post_SeaEquipPrep':
                                        (u'Seafloor preparation + support '
                                         'structure positioning and equipment '
                                         'preparation'),
                                    u'PreLay': u'Pre-lay moorings or buoy off',
                                    u'Pre_SeaEquipPrep':
                                        (u'Guiding template positioning + '
                                         'seafloor preparation equipment '
                                         'preparation'),
                                    u'Seafast': u'Seafastening',
                                    u'SeafloorEquipPrep':
                                        u'Seafloor & equipment preparation',
                                    u'Splice_Connect':
                                        u'Conduct splice connection on deck',
                                    u'SuppStrutPos':
                                        u'Support structure positioning',
                                    u'TowTrans': u'Towing transportation',
                                    u'TranPortSite':
                                        u'Transportation from port to site',
                                    u'TranSitePort':
                                        u'Transportation from site to port',
                                    u'TranSiteSite':
                                        u'Transportation from site to site',
                                    u'VesPos': u'Vessel Positioning',
                                    u'VesPosCables': u'Vessel Positioning',
                                    u'VessPrep':
                                        u'Vessel preparation & loading',
                                    u'VessPrep_SeabedCP':
                                        (u'Vessel preparation & loading of '
                                         'individual seabed collection '
                                         'points'),
                                    u'VessPrep_SurfaceCP':
                                        (u'Vessel preparation & loading of '
                                         'individual surface piercing '
                                         'collection points'),
                                    u'VessPrep_direct':
                                        (u'Vessel preparation & loading of '
                                         'individual direct-embedment '
                                         'anchors'),
                                    u'VessPrep_drag': 
                                        (u'Vessel preparation & loading of '
                                         'individual drag-embedment anchors'),
                                    u'VessPrep_driven':
                                        (u'Vessel preparation & loading of '
                                         'individual driven piles'),
                                    u'VessPrep_external':
                                        (u'Vessel preparation & loading of '
                                         'individual external protection '
                                         'equipment stacks'),
                                    u'VessPrep_gravity':
                                        (u'Vessel preparation & loading of '
                                         'individual gravity based '
                                         'foundations'),
                                    u'VessPrep_pile':
                                        (u'Vessel preparation & loading of '
                                         'individual pile anchors'),
                                    u'VessPrep_suction':
                                        (u'Vessel preparation & loading of '
                                         'individual suction-embedment '
                                         'anchors'),
                                    u'VessPrep_support':
                                        (u'Vessel preparation & loading of '
                                         'individual support structures'),
                                    u'Wet_Connect':
                                        (u'Connect to guide wire + Lower '
                                         'cable and connection equip + '
                                         'Perform wet-mate connect + Recover '
                                         'connection equip')
                                        },
         u'OLC: Cs [m/s]': {u'Access': u"om['Cs_acc [m/s]']",
                            u'AssPort': np.nan,
                            u'BurialToolDeploy': 2.0,
                            u'BurialToolRecov': 2.0,
                            u'CableLay_Burial': 2.0,
                            u'CableLay_Dyn': 2.0,
                            u'CableLay_Route': 2.0,
                            u'CableLay_SplitPipe': 2.0,
                            u'CableLay_Trench': 2.0,
                            u'CaissonSuct': np.nan,
                            u'ConnectPile': 2.0,
                            u'Connect_Topside': 2.0,
                            u'DeckTrans': u'vessel',
                            u'Demob': np.nan,
                            u'DevAssPort': np.nan,
                            u'DirecJet': 2.0,
                            u'DirecMech': 2.0,
                            u'DirecSuct': 2.0,
                            u'DragEmbed': 2.0,
                            u'Dry_Connect': np.nan,
                            u'GBSlow': 2.0,
                            u'GBSpos': np.nan,
                            u'Grout': 2.0,
                            u'GroutRemov': 2.0,
                            u'HDD': 2.0,
                            u'Install_mattress': 2.0,
                            u'Install_rockbag': 2.0,
                            u'Jtube_Connect': 2.0,
                            u'Lift_Cable_Seabed': 2.0,
                            u'Lift_Topside': 2.0,
                            u'LoadCableFactory': np.nan,
                            u'LoadOut_Float': np.nan,
                            u'LoadOut_Lift': np.nan,
                            u'LoadOut_Skidded': np.nan,
                            u'Lower_CP_Seabed': 2.0,
                            u'Lower_Cable_Seabed': 2.0,
                            u'Maintenance': u"om['Cs_om [m/s]']",
                            u'Mob': np.nan,
                            u'OCT': 2.0,
                            u'PileDrill': 2.0,
                            u'PileHamm': 2.0,
                            u'PileVibro': 2.0,
                            u'PosBFdev': u"device['max Cs [m/s]']",
                            u'PosFLTdev': u"device['max Cs [m/s]']",
                            u'Post_SeaEquipPrep': 2.0,
                            u'PreLay': np.nan,
                            u'Pre_SeaEquipPrep': 2.0,
                            u'Seafast': np.nan,
                            u'SeafloorEquipPrep': 2.0,
                            u'Splice_Connect': np.nan,
                            u'SuppStrutPos': u'vessel',
                            u'TowTrans': u'vessel',
                            u'TranPortSite': u'vessel',
                            u'TranSitePort': u'vessel',
                            u'TranSiteSite': u'vessel',
                            u'VesPos': u'vessel',
                            u'VesPosCables': u'vessel',
                            u'VessPrep': np.nan,
                            u'VessPrep_SeabedCP': np.nan,
                            u'VessPrep_SurfaceCP': np.nan,
                            u'VessPrep_direct': np.nan,
                            u'VessPrep_drag': np.nan,
                            u'VessPrep_driven': np.nan,
                            u'VessPrep_external': np.nan,
                            u'VessPrep_gravity': np.nan,
                            u'VessPrep_pile': np.nan,
                            u'VessPrep_suction': np.nan,
                            u'VessPrep_support': np.nan,
                            u'Wet_Connect': 2.0},
         u'OLC: Hs [m]': {u'Access': u"om['Hs_acc [m]']",
                          u'AssPort': np.nan,
                          u'BurialToolDeploy': 3.0,
                          u'BurialToolRecov': 3.0,
                          u'CableLay_Burial': 3.0,
                          u'CableLay_Dyn': 3.0,
                          u'CableLay_Route': 3.0,
                          u'CableLay_SplitPipe': 3.0,
                          u'CableLay_Trench': 3.0,
                          u'CaissonSuct': np.nan,
                          u'ConnectPile': np.nan,
                          u'Connect_Topside': 3.0,
                          u'DeckTrans': u'vessel',
                          u'Demob': np.nan,
                          u'DevAssPort': np.nan,
                          u'DirecJet': np.nan,
                          u'DirecMech': np.nan,
                          u'DirecSuct': np.nan,
                          u'DragEmbed': np.nan,
                          u'Dry_Connect': 3.0,
                          u'GBSlow': np.nan,
                          u'GBSpos': np.nan,
                          u'Grout': np.nan,
                          u'GroutRemov': np.nan,
                          u'HDD': 3.0,
                          u'Install_mattress': 3.0,
                          u'Install_rockbag': 3.0,
                          u'Jtube_Connect': 3.0,
                          u'Lift_Cable_Seabed': 3.0,
                          u'Lift_Topside': 3.0,
                          u'LoadCableFactory': np.nan,
                          u'LoadOut_Float': np.nan,
                          u'LoadOut_Lift': np.nan,
                          u'LoadOut_Skidded': np.nan,
                          u'Lower_CP_Seabed': 3.0,
                          u'Lower_Cable_Seabed': 3.0,
                          u'Maintenance': u"om['Hs_om [m]']",
                          u'Mob': np.nan,
                          u'OCT': 3.0,
                          u'PileDrill': np.nan,
                          u'PileHamm': np.nan,
                          u'PileVibro': np.nan,
                          u'PosBFdev': u"device['max Hs [m]']",
                          u'PosFLTdev': u"device['max Hs [m]']",
                          u'Post_SeaEquipPrep': np.nan,
                          u'PreLay': np.nan,
                          u'Pre_SeaEquipPrep': np.nan,
                          u'Seafast': np.nan,
                          u'SeafloorEquipPrep': u'vessel',
                          u'Splice_Connect': 3.0,
                          u'SuppStrutPos': u'vessel',
                          u'TowTrans': u'vessel',
                          u'TranPortSite': u'vessel',
                          u'TranSitePort': u'vessel',
                          u'TranSiteSite': u'vessel',
                          u'VesPos': u'vessel',
                          u'VesPosCables': u'vessel',
                          u'VessPrep': np.nan,
                          u'VessPrep_SeabedCP': np.nan,
                          u'VessPrep_SurfaceCP': np.nan,
                          u'VessPrep_direct': np.nan,
                          u'VessPrep_drag': np.nan,
                          u'VessPrep_driven': np.nan,
                          u'VessPrep_external': np.nan,
                          u'VessPrep_gravity': np.nan,
                          u'VessPrep_pile': np.nan,
                          u'VessPrep_suction': np.nan,
                          u'VessPrep_support': np.nan,
                          u'Wet_Connect': 3.0},
         u'OLC: Other [-]': {u'Access': np.nan,
                             u'AssPort': np.nan,
                             u'BurialToolDeploy': np.nan,
                             u'BurialToolRecov': np.nan,
                             u'CableLay_Burial': np.nan,
                             u'CableLay_Dyn': np.nan,
                             u'CableLay_Route': np.nan,
                             u'CableLay_SplitPipe': np.nan,
                             u'CableLay_Trench': np.nan,
                             u'CaissonSuct': np.nan,
                             u'ConnectPile': np.nan,
                             u'Connect_Topside': np.nan,
                             u'DeckTrans': np.nan,
                             u'Demob': np.nan,
                             u'DevAssPort': np.nan,
                             u'DirecJet': np.nan,
                             u'DirecMech': np.nan,
                             u'DirecSuct': np.nan,
                             u'DragEmbed': np.nan,
                             u'Dry_Connect': np.nan,
                             u'GBSlow': np.nan,
                             u'GBSpos': np.nan,
                             u'Grout': np.nan,
                             u'GroutRemov': np.nan,
                             u'HDD': np.nan,
                             u'Install_mattress': np.nan,
                             u'Install_rockbag': np.nan,
                             u'Jtube_Connect': np.nan,
                             u'Lift_Cable_Seabed': np.nan,
                             u'Lift_Topside': np.nan,
                             u'LoadCableFactory': np.nan,
                             u'LoadOut_Float': np.nan,
                             u'LoadOut_Lift': np.nan,
                             u'LoadOut_Skidded': np.nan,
                             u'Lower_CP_Seabed': np.nan,
                             u'Lower_Cable_Seabed': np.nan,
                             u'Maintenance': np.nan,
                             u'Mob': np.nan,
                             u'OCT': np.nan,
                             u'PileDrill': np.nan,
                             u'PileHamm': np.nan,
                             u'PileVibro': np.nan,
                             u'PosBFdev': u'end-user',
                             u'PosFLTdev': u'end-user',
                             u'Post_SeaEquipPrep': np.nan,
                             u'PreLay': np.nan,
                             u'Pre_SeaEquipPrep': np.nan,
                             u'Seafast': np.nan,
                             u'SeafloorEquipPrep': np.nan,
                             u'Splice_Connect': np.nan,
                             u'SuppStrutPos': np.nan,
                             u'TowTrans': np.nan,
                             u'TranPortSite': np.nan,
                             u'TranSitePort': np.nan,
                             u'TranSiteSite': np.nan,
                             u'VesPos': np.nan,
                             u'VesPosCables': np.nan,
                             u'VessPrep': np.nan,
                             u'VessPrep_SeabedCP': np.nan,
                             u'VessPrep_SurfaceCP': np.nan,
                             u'VessPrep_direct': np.nan,
                             u'VessPrep_drag': np.nan,
                             u'VessPrep_driven': np.nan,
                             u'VessPrep_external': np.nan,
                             u'VessPrep_gravity': np.nan,
                             u'VessPrep_pile': np.nan,
                             u'VessPrep_suction': np.nan,
                             u'VessPrep_support': np.nan,
                             u'Wet_Connect': np.nan},
         u'OLC: Tp [s]': {u'Access': u"om['Tp_acc [s]']",
                          u'AssPort': np.nan,
                          u'BurialToolDeploy': 15.0,
                          u'BurialToolRecov': 15.0,
                          u'CableLay_Burial': 15.0,
                          u'CableLay_Dyn': 15.0,
                          u'CableLay_Route': 15.0,
                          u'CableLay_SplitPipe': 15.0,
                          u'CableLay_Trench': 15.0,
                          u'CaissonSuct': np.nan,
                          u'ConnectPile': 15.0,
                          u'Connect_Topside': 15.0,
                          u'DeckTrans': u'vessel',
                          u'Demob': np.nan,
                          u'DevAssPort': np.nan,
                          u'DirecJet': 15.0,
                          u'DirecMech': 15.0,
                          u'DirecSuct': 15.0,
                          u'DragEmbed': 15.0,
                          u'Dry_Connect': 15.0,
                          u'GBSlow': 15.0,
                          u'GBSpos': np.nan,
                          u'Grout': 15.0,
                          u'GroutRemov': 15.0,
                          u'HDD': 15.0,
                          u'Install_mattress': 15.0,
                          u'Install_rockbag': 15.0,
                          u'Jtube_Connect': 15.0,
                          u'Lift_Cable_Seabed': 15.0,
                          u'Lift_Topside': 15.0,
                          u'LoadCableFactory': np.nan,
                          u'LoadOut_Float': np.nan,
                          u'LoadOut_Lift': np.nan,
                          u'LoadOut_Skidded': np.nan,
                          u'Lower_CP_Seabed': 15.0,
                          u'Lower_Cable_Seabed': 15.0,
                          u'Maintenance': u"om['Tp_om [s]']",
                          u'Mob': np.nan,
                          u'OCT': 15.0,
                          u'PileDrill': 15.0,
                          u'PileHamm': 15.0,
                          u'PileVibro': 15.0,
                          u'PosBFdev': u"device['max Tp [s]']",
                          u'PosFLTdev': u"device['max Tp [s]']",
                          u'Post_SeaEquipPrep': 15.0,
                          u'PreLay': np.nan,
                          u'Pre_SeaEquipPrep': 15.0,
                          u'Seafast': np.nan,
                          u'SeafloorEquipPrep': 15.0,
                          u'Splice_Connect': 15.0,
                          u'SuppStrutPos': u'vessel',
                          u'TowTrans': u'vessel',
                          u'TranPortSite': u'vessel',
                          u'TranSitePort': u'vessel',
                          u'TranSiteSite': u'vessel',
                          u'VesPos': u'vessel',
                          u'VesPosCables': u'vessel',
                          u'VessPrep': np.nan,
                          u'VessPrep_SeabedCP': np.nan,
                          u'VessPrep_SurfaceCP': np.nan,
                          u'VessPrep_direct': np.nan,
                          u'VessPrep_drag': np.nan,
                          u'VessPrep_driven': np.nan,
                          u'VessPrep_external': np.nan,
                          u'VessPrep_gravity': np.nan,
                          u'VessPrep_pile': np.nan,
                          u'VessPrep_suction': np.nan,
                          u'VessPrep_support': np.nan,
                          u'Wet_Connect': 15.0},
         u'OLC: Ws [m/s]': {u'Access': u"om['Ws_acc  [m/s]']",
                            u'AssPort': np.nan,
                            u'BurialToolDeploy': 20.0,
                            u'BurialToolRecov': 20.0,
                            u'CableLay_Burial': 20.0,
                            u'CableLay_Dyn': 20.0,
                            u'CableLay_Route': 20.0,
                            u'CableLay_SplitPipe': 20.0,
                            u'CableLay_Trench': 20.0,
                            u'CaissonSuct': np.nan,
                            u'ConnectPile': 20.0,
                            u'Connect_Topside': 20.0,
                            u'DeckTrans': u'vessel',
                            u'Demob': np.nan,
                            u'DevAssPort': np.nan,
                            u'DirecJet': 20.0,
                            u'DirecMech': 20.0,
                            u'DirecSuct': 20.0,
                            u'DragEmbed': 20.0,
                            u'Dry_Connect': 20.0,
                            u'GBSlow': 20.0,
                            u'GBSpos': np.nan,
                            u'Grout': 20.0,
                            u'GroutRemov': 20.0,
                            u'HDD': 20.0,
                            u'Install_mattress': 20.0,
                            u'Install_rockbag': 20.0,
                            u'Jtube_Connect': 20.0,
                            u'Lift_Cable_Seabed': 20.0,
                            u'Lift_Topside': 20.0,
                            u'LoadCableFactory': np.nan,
                            u'LoadOut_Float': np.nan,
                            u'LoadOut_Lift': np.nan,
                            u'LoadOut_Skidded': np.nan,
                            u'Lower_CP_Seabed': 20.0,
                            u'Lower_Cable_Seabed': 20.0,
                            u'Maintenance': u"om['Ws_om  [m/s]']",
                            u'Mob': np.nan,
                            u'OCT': 20.0,
                            u'PileDrill': 20.0,
                            u'PileHamm': 20.0,
                            u'PileVibro': 20.0,
                            u'PosBFdev': u"device['max Ws [m/s]']",
                            u'PosFLTdev': u"device['max Ws [m/s]']",
                            u'Post_SeaEquipPrep': 20.0,
                            u'PreLay': np.nan,
                            u'Pre_SeaEquipPrep': 20.0,
                            u'Seafast': np.nan,
                            u'SeafloorEquipPrep': 20.0,
                            u'Splice_Connect': 20.0,
                            u'SuppStrutPos': u'vessel',
                            u'TowTrans': u'vessel',
                            u'TranPortSite': u'vessel',
                            u'TranSitePort': u'vessel',
                            u'TranSiteSite': u'vessel',
                            u'VesPos': u'vessel',
                            u'VesPosCables': u'vessel',
                            u'VessPrep': np.nan,
                            u'VessPrep_SeabedCP': np.nan,
                            u'VessPrep_SurfaceCP': np.nan,
                            u'VessPrep_direct': np.nan,
                            u'VessPrep_drag': np.nan,
                            u'VessPrep_driven': np.nan,
                            u'VessPrep_external': np.nan,
                            u'VessPrep_gravity': np.nan,
                            u'VessPrep_pile': np.nan,
                            u'VessPrep_suction': np.nan,
                            u'VessPrep_support': np.nan,
                            u'Wet_Connect': 20.0},
         u'Time: function [-]': {u'Access': np.nan,
                                 u'AssPort': np.nan,
                                 u'BurialToolDeploy': np.nan,
                                 u'BurialToolRecov': np.nan,
                                 u'CableLay_Burial': u'burial_time',
                                 u'CableLay_Dyn': u'surface_time',
                                 u'CableLay_Route': u'surface_time',
                                 u'CableLay_SplitPipe': u'pipe_time',
                                 u'CableLay_Trench': u'surface_time',
                                 u'CaissonSuct': u'penetration_time',
                                 u'ConnectPile': np.nan,
                                 u'Connect_Topside': np.nan,
                                 u'DeckTrans': u'transit_algorithm',
                                 u'Demob': np.nan,
                                 u'DevAssPort': np.nan,
                                 u'DirecJet': u'penetration_time',
                                 u'DirecMech': u'penetration_time',
                                 u'DirecSuct': u'penetration_time',
                                 u'DragEmbed': np.nan,
                                 u'Dry_Connect': np.nan,
                                 u'GBSlow': u'lowering',
                                 u'GBSpos': np.nan,
                                 u'Grout': u'grouting',
                                 u'GroutRemov': np.nan,
                                 u'HDD': np.nan,
                                 u'Install_mattress': np.nan,
                                 u'Install_rockbag': np.nan,
                                 u'Jtube_Connect': np.nan,
                                 u'Lift_Cable_Seabed': np.nan,
                                 u'Lift_Topside': np.nan,
                                 u'LoadCableFactory': u'load_cable',
                                 u'LoadOut_Float': np.nan,
                                 u'LoadOut_Lift': np.nan,
                                 u'LoadOut_Skidded': np.nan,
                                 u'Lower_CP_Seabed': np.nan,
                                 u'Lower_Cable_Seabed': np.nan,
                                 u'Maintenance': np.nan,
                                 u'Mob': np.nan,
                                 u'OCT': np.nan,
                                 u'PileDrill': u'penetration_time',
                                 u'PileHamm': u'penetration_time',
                                 u'PileVibro': u'penetration_time',
                                 u'PosBFdev': np.nan,
                                 u'PosFLTdev': np.nan,
                                 u'Post_SeaEquipPrep': np.nan,
                                 u'PreLay': np.nan,
                                 u'Pre_SeaEquipPrep': np.nan,
                                 u'Seafast': np.nan,
                                 u'SeafloorEquipPrep': np.nan,
                                 u'Splice_Connect': np.nan,
                                 u'SuppStrutPos': np.nan,
                                 u'TowTrans': u'transit_algorithm',
                                 u'TranPortSite': u'transit_algorithm',
                                 u'TranSitePort': u'transit_algorithm',
                                 u'TranSiteSite': u'distance',
                                 u'VesPos': np.nan,
                                 u'VesPosCables': np.nan,
                                 u'VessPrep': np.nan,
                                 u'VessPrep_SeabedCP': np.nan,
                                 u'VessPrep_SurfaceCP': np.nan,
                                 u'VessPrep_direct': np.nan,
                                 u'VessPrep_drag': np.nan,
                                 u'VessPrep_driven': np.nan,
                                 u'VessPrep_external': np.nan,
                                 u'VessPrep_gravity': np.nan,
                                 u'VessPrep_pile': np.nan,
                                 u'VessPrep_suction': np.nan,
                                 u'VessPrep_support': np.nan,
                                 u'Wet_Connect': np.nan},
         u'Time: other [-]': {u'Access': u"om['d_acc [hour]']",
                              u'AssPort': np.nan,
                              u'BurialToolDeploy': np.nan,
                              u'BurialToolRecov': np.nan,
                              u'CableLay_Burial': np.nan,
                              u'CableLay_Dyn': np.nan,
                              u'CableLay_Route': np.nan,
                              u'CableLay_SplitPipe': np.nan,
                              u'CableLay_Trench': np.nan,
                              u'CaissonSuct': np.nan,
                              u'ConnectPile': np.nan,
                              u'Connect_Topside': np.nan,
                              u'DeckTrans': np.nan,
                              u'Demob': u"vesselsDB['Mob time [h]']",
                              u'DevAssPort':
                                  u"device['assembly duration [h]']",
                              u'DirecJet': np.nan,
                              u'DirecMech': np.nan,
                              u'DirecSuct': np.nan,
                              u'DragEmbed': np.nan,
                              u'Dry_Connect': np.nan,
                              u'GBSlow': np.nan,
                              u'GBSpos': np.nan,
                              u'Grout': np.nan,
                              u'GroutRemov': np.nan,
                              u'HDD': np.nan,
                              u'Install_mattress': np.nan,
                              u'Install_rockbag': np.nan,
                              u'Jtube_Connect': np.nan,
                              u'Lift_Cable_Seabed': np.nan,
                              u'Lift_Topside': np.nan,
                              u'LoadCableFactory': np.nan,
                              u'LoadOut_Float': np.nan,
                              u'LoadOut_Lift': np.nan,
                              u'LoadOut_Skidded': np.nan,
                              u'Lower_CP_Seabed': np.nan,
                              u'Lower_Cable_Seabed': np.nan,
                              u'Maintenance': u"om['d_om [hour]']",
                              u'Mob': u"vesselsDB['Mob time [h]']",
                              u'OCT': np.nan,
                              u'PileDrill': np.nan,
                              u'PileHamm': np.nan,
                              u'PileVibro': np.nan,
                              u'PosBFdev': u"device['connect duration [h]']",
                              u'PosFLTdev': u"device['connect duration [h]']",
                              u'Post_SeaEquipPrep': np.nan,
                              u'PreLay': np.nan,
                              u'Pre_SeaEquipPrep': np.nan,
                              u'Seafast': np.nan,
                              u'SeafloorEquipPrep': np.nan,
                              u'Splice_Connect': np.nan,
                              u'SuppStrutPos': np.nan,
                              u'TowTrans': np.nan,
                              u'TranPortSite': np.nan,
                              u'TranSitePort': np.nan,
                              u'TranSiteSite': np.nan,
                              u'VesPos': np.nan,
                              u'VesPosCables': np.nan,
                              u'VessPrep': np.nan,
                              u'VessPrep_SeabedCP': np.nan,
                              u'VessPrep_SurfaceCP': np.nan,
                              u'VessPrep_direct': np.nan,
                              u'VessPrep_drag': np.nan,
                              u'VessPrep_driven': np.nan,
                              u'VessPrep_external': np.nan,
                              u'VessPrep_gravity': np.nan,
                              u'VessPrep_pile': np.nan,
                              u'VessPrep_suction': np.nan,
                              u'VessPrep_support': np.nan,
                              u'Wet_Connect': np.nan},
         u'Time: value [h]': {u'Access': np.nan,
                              u'AssPort': 1.0,
                              u'BurialToolDeploy': 2.0,
                              u'BurialToolRecov': 2.0,
                              u'CableLay_Burial': np.nan,
                              u'CableLay_Dyn': np.nan,
                              u'CableLay_Route': np.nan,
                              u'CableLay_SplitPipe': np.nan,
                              u'CableLay_Trench': np.nan,
                              u'CaissonSuct': np.nan,
                              u'ConnectPile': 0.5,
                              u'Connect_Topside': 10.0,
                              u'DeckTrans': np.nan,
                              u'Demob': np.nan,
                              u'DevAssPort': np.nan,
                              u'DirecJet': np.nan,
                              u'DirecMech': np.nan,
                              u'DirecSuct': np.nan,
                              u'DragEmbed': 1.5,
                              u'Dry_Connect': 0.5,
                              u'GBSlow': np.nan,
                              u'GBSpos': 1.0,
                              u'Grout': 0.5,
                              u'GroutRemov': 0.5,
                              u'HDD': 4.5,
                              u'Install_mattress': 0.5,
                              u'Install_rockbag': 0.5,
                              u'Jtube_Connect': 2.0,
                              u'Lift_Cable_Seabed': 1.75,
                              u'Lift_Topside': 5.0,
                              u'LoadCableFactory': np.nan,
                              u'LoadOut_Float': 4.0,
                              u'LoadOut_Lift': 1.0,
                              u'LoadOut_Skidded': 2.0,
                              u'Lower_CP_Seabed': 2.0,
                              u'Lower_Cable_Seabed': 0.75,
                              u'Maintenance': np.nan,
                              u'Mob': np.nan,
                              u'OCT': 4.5,
                              u'PileDrill': np.nan,
                              u'PileHamm': np.nan,
                              u'PileVibro': np.nan,
                              u'PosBFdev': np.nan,
                              u'PosFLTdev': np.nan,
                              u'Post_SeaEquipPrep': 2.0,
                              u'PreLay': 0.5,
                              u'Pre_SeaEquipPrep': 2.0,
                              u'Seafast': 0.5,
                              u'SeafloorEquipPrep': 1.0,
                              u'Splice_Connect': 0.5,
                              u'SuppStrutPos': 2.0,
                              u'TowTrans': np.nan,
                              u'TranPortSite': np.nan,
                              u'TranSitePort': np.nan,
                              u'TranSiteSite': np.nan,
                              u'VesPos': 6.0,
                              u'VesPosCables': 1.0,
                              u'VessPrep': 48.0,
                              u'VessPrep_SeabedCP': 12.0,
                              u'VessPrep_SurfaceCP': 48.0,
                              u'VessPrep_direct': 4.0,
                              u'VessPrep_drag': 4.0,
                              u'VessPrep_driven': 4.0,
                              u'VessPrep_external': 4.0,
                              u'VessPrep_gravity': 4.0,
                              u'VessPrep_pile': 4.0,
                              u'VessPrep_suction': 4.0,
                              u'VessPrep_support': 12.0,
                              u'Wet_Connect': 2.0},
         u'id [-]': {u'Access': 600,
                     u'AssPort': 101,
                     u'BurialToolDeploy': 203,
                     u'BurialToolRecov': 204,
                     u'CableLay_Burial': 205,
                     u'CableLay_Dyn': 209,
                     u'CableLay_Route': 206,
                     u'CableLay_SplitPipe': 208,
                     u'CableLay_Trench': 207,
                     u'CaissonSuct': 402,
                     u'ConnectPile': 401,
                     u'Connect_Topside': 218,
                     u'DeckTrans': 505,
                     u'Demob': 116,
                     u'DevAssPort': 500,
                     u'DirecJet': 404,
                     u'DirecMech': 405,
                     u'DirecSuct': 403,
                     u'DragEmbed': 400,
                     u'Dry_Connect': 210,
                     u'GBSlow': 306,
                     u'GBSpos': 305,
                     u'Grout': 118,
                     u'GroutRemov': 119,
                     u'HDD': 202,
                     u'Install_mattress': 219,
                     u'Install_rockbag': 220,
                     u'Jtube_Connect': 213,
                     u'Lift_Cable_Seabed': 215,
                     u'Lift_Topside': 217,
                     u'LoadCableFactory': 200,
                     u'LoadOut_Float': 503,
                     u'LoadOut_Lift': 501,
                     u'LoadOut_Skidded': 502,
                     u'Lower_CP_Seabed': 216,
                     u'Lower_Cable_Seabed': 214,
                     u'Maintenance': 601,
                     u'Mob': 100,
                     u'OCT': 201,
                     u'PileDrill': 302,
                     u'PileHamm': 303,
                     u'PileVibro': 304,
                     u'PosBFdev': 507,
                     u'PosFLTdev': 508,
                     u'Post_SeaEquipPrep': 301,
                     u'PreLay': 406,
                     u'Pre_SeaEquipPrep': 300,
                     u'Seafast': 504,
                     u'SeafloorEquipPrep': 117,
                     u'Splice_Connect': 211,
                     u'SuppStrutPos': 122,
                     u'TowTrans': 506,
                     u'TranPortSite': 113,
                     u'TranSitePort': 114,
                     u'TranSiteSite': 115,
                     u'VesPos': 120,
                     u'VesPosCables': 121,
                     u'VessPrep': 102,
                     u'VessPrep_SeabedCP': 109,
                     u'VessPrep_SurfaceCP': 110,
                     u'VessPrep_direct': 107,
                     u'VessPrep_drag': 106,
                     u'VessPrep_driven': 111,
                     u'VessPrep_external': 112,
                     u'VessPrep_gravity': 108,
                     u'VessPrep_pile': 105,
                     u'VessPrep_suction': 104,
                     u'VessPrep_support': 103,
                     u'Wet_Connect': 212}}
         
    op_db = pd.DataFrame(x)
    
    return op_db


def test_LogOp_init():
    
    test = LogOp(None,
                 None,
                 None,
                 None,
                 None,
                 None)
    
    assert test
    

def test_logOp_init(op_db):
    
    test = logOp_init(op_db)
    random_key = random.choice(test.keys())
        
    assert isinstance(test[random_key], LogOp)
    assert len(test) == len(op_db)
