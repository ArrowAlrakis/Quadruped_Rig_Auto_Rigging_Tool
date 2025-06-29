# ---------------------------------------------------------------------------------------
# Python Auto-Rig Tool for Quadruped Creatures
# Developed by Arrow Lyu
#
# ---------------------------------------------------------------------------------------
# This auto rigging script is designed for quadruped creatures and includes customizable
# modules such as fins, spines, crests, and tail extensions. Originally built and adapted
# by me, this version was tailored specifically for my dragon character Rimerock.
#
# The rig is based on Python modules and concepts learned from my professor Dennis Turner.
# Some module structures are quoted with permission and adapted for this use.
#
# This tool is flexible and can be adapted to any four-legged creature.
#
# How to Use:
# 1. Customize the joint count for neck, spine, or tail as needed.
# 2. Manually place the locators to match your character’s proportions.
# 3. Select which modules to add or remove.
# 4. Run the script and start painting weights.
#
# === USER PARAMETERS ===
# neck_joints = 6
# spine_joints = 3
# tail_joints = 8
# has_spikes = True
# has_fins = True
# has_crest = True
# has_whisker = True
# render_mesh_name = "Rimerock_Geo"
# proxy_mesh_name = "Rimerock_Mesh"
# box_mesh_name = "Rimerock_Box"
# =======================
#
# Happy rigging!
# ---------------------------------------------------------------------------------------
# (c) 2025 by Arrow Lyu. All rights reserved. For portfolio and educational use only.
# ---------------------------------------------------------------------------------------


import sys; sys.dont_write_bytecode=True
import maya.cmds as cmds
import maya.mel as mel
import maya.api.OpenMaya as om
import importlib

import den_Utilities_v12 as denUt
importlib.reload(denUt)
print(denUt.__file__)

import den_BipedRigTools_v12 as denBR
importlib.reload(denBR)
print(denBR.__file__)

import den_SluggyRigTools_v12 as denSR
importlib.reload(denSR)
print(denSR.__file__)

import den_TrexRigTools_v12 as denTR
importlib.reload(denTR)
print(denTR.__file__)

import den_AutoRigTools_v12 as denAR
importlib.reload(denAR)
print(denAR.__file__)


# ---------------------------------------------------------------------------------------
# Start
# find the path of the current project/workspace, for reading data files such as skinClusters and ATOM animation later
projDir = cmds.workspace( q=True, rootDirectory=True )
print( projDir )

denUt.den_DiagPause( seconds=0.01 )

# set the rig name as the name of the creature
rigName = 'Rimerock'


# ---------------------------------------------------------------------------------------
# make base pivot for master rig group

BasePivRet = denBR.den_makeBasePiv( name=rigName, radius=5 )
print( BasePivRet )
# capture the master pivot group in a variable, RootPivGrp will contain all other pivot groups
RootPivGrp = BasePivRet

# position the cog pivot
cmds.xform( 'Cog_Piv', t=( 0.0, 120.00702247157264, -5.048634273151116 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )

# ---------------------------------------------------------------------------------------
# make base rig

BaseRigRet = denBR.den_makeBaseRig(label=rigName,ctrlRadius=150.0)
print( BaseRigRet )
# capture the master rig group in a variable, RootRigGrp will contain all other smaller rig groups 
RootRigGrp = BaseRigRet[0]; print( RootRigGrp )
# capture spaceIn, spaceOUT, BindJoints, Controls, and Guts in 5 variables
BaseSpaceINs = BaseRigRet[1]; print( BaseSpaceINs )
BaseSpaceOUTs = BaseRigRet[2]; print( BaseSpaceOUTs )
BaseBindJnts = BaseRigRet[3]; print( BaseBindJnts )
BaseCtrlsALL = BaseRigRet[4]; print( BaseCtrlsALL )
BaseGutsALL = BaseRigRet[5]; print( BaseGutsALL )

# added for later, so trex leg can function, and we can connect rig visibility attribute to all control
CogSpaceOUT = BaseSpaceOUTs[0]
AllSpaceOUT = BaseSpaceOUTs[1]
AllCtrl = BaseCtrlsALL[2]

# connect geometry visibility attribute to the All_Ctrl
#cmds.connectAttr( AllCtrl+'.Show_Box_Geo', 'Boxes_Grp.visibility' )  # include this if you use box geometry
cmds.connectAttr( AllCtrl+'.Show_Proxy_Geo', 'Proxies_Grp.visibility' )
cmds.connectAttr( AllCtrl+'.Show_Render_Geo', 'Render_Grp.visibility' )

# ---------------------------------------------------------------------------------------
# make any-torso pivot

TorsoPivRet = denAR.den_makeAnyTorsoPivs( prefix='', radius=5.0, spineCount=3, neckCount=6, dpTime=0.01 )
print( TorsoPivRet )

# capture all pivots in a variable
TorsoPivGrp = TorsoPivRet

# parent pivots under root pivot group
cmds.parent( TorsoPivGrp, RootPivGrp ) 

# position torso pivots
cmds.xform( 'Spine01_Piv', t=( 0.0, 133.25360534938514, -49.29973644608609 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'Spine02_Piv', t=( 0.0, 130.10030622113092, -22.885349571582843 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'Spine03_Piv', t=( 0.0, 124.60231328074619, 8.663615384691786 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'Neck01_Piv', t=( 0.0, 143.34632132305936, 73.57294986173603 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'Neck02_Piv', t=( 0.0, 162.10635480630066, 99.91028076083076 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'Neck03_Piv', t=( 0.0, 178.7424559716574, 117.00434284660463 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'Neck04_Piv', t=( 0.0, 195.18059911506734, 141.16029203095454 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'Neck05_Piv', t=( 0.0, 207.86811314571392, 165.95032123872315 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'Neck06_Piv', t=( 0.0, 209.58951328713806, 196.49836424943382 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'Pelvis_Piv', t=( 0.0, 133.39426932604795, -87.36977679246662 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'Chest_Piv', t=( 0.0, 128.5279535441665, 46.64251001336936 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'Head_Piv', t=( 0.0, 208.03742911780915, 223.37096545059103 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'HeadEnd_Piv', t=( 0.0, 200.1864811785, 245.74096939071057 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'Jaw_Piv', t=( 0.0, 201.66972992782308, 213.44114471371418 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'JawEnd_Piv', t=( 0.0, 175.77796616967277, 231.79762889869127 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )



# ---------------------------------------------------------------------------------------
# make any-torso rig 

TorsoRigRet = denAR.den_makeAnyTorsoRig( prefix='', radius=5.0, ctrlRadius=(40.0,55.0,25.0,5.0), displayLocalAxis=False, spineCount=3, spineSecondaryJoints=[], neckCount=6, neckSecondaryJoints=[4], spineAxisOrient='yup', jawAxisOrient='yup', dpTime=0.01 )
print( TorsoRigRet )

# capture the rig group in a variable
TorsoRigGrp = TorsoRigRet[0]; print( TorsoRigGrp )
# capture spaceIn, spaceOUT, BindJoints, Controls, and Guts in 5 variables
TorsoSpaceINs = TorsoRigRet[1]; print( TorsoSpaceINs )
TorsoSpaceOUTs = TorsoRigRet[2]; print( TorsoSpaceOUTs )
TorsoBindJnts = TorsoRigRet[3]; print( TorsoBindJnts )
TorsoCtrlsALL = TorsoRigRet[4]; print( TorsoCtrlsALL )
TorsoGutsALL = TorsoRigRet[5]; print( TorsoGutsALL )

# make new variables for later connecting attributes
TorsoSpaceIN = TorsoSpaceINs[0]; print( TorsoSpaceIN )
PelvisSpaceOUT = TorsoSpaceOUTs[0]; print( PelvisSpaceOUT )

#### ======== NEED TO EDIT THIS IF YOU CHANGED THE NUMBER OF NECK/SPINE JOINTS ======== ####
# i changed the number in [] since the torso spine number is changed by -2
ChestSpaceOUT = TorsoSpaceOUTs[4]; print( ChestSpaceOUT )
HeadSpaceOUT = TorsoSpaceOUTs[11]; print( HeadSpaceOUT )
JawSpaceOUT = TorsoSpaceOUTs[12]; print( JawSpaceOUT )

# connect to geometry
#denUt.den_connectBoxGeo( Jnts=TorsoBindJnts ) # include this if you use box geometry
denUt.den_connectProxyGeo( Jnts=TorsoBindJnts )

# parent rig under root rig group
TorsoRigGrp = cmds.parent( TorsoRigGrp, RootRigGrp )

# capture cog spaceOut in a new variables
print( BaseSpaceOUTs )
CogSpaceOUT = BaseSpaceOUTs[0]
# Connect translate/rotate/scale of spaceINs to its spaceOUTs with constraint
cmds.parentConstraint( CogSpaceOUT, TorsoSpaceIN, mo=True )
cmds.scaleConstraint( CogSpaceOUT, TorsoSpaceIN, mo=True )

# add safetycovers and etc.
denUt.den_AddSafetyCovers( rigGroup=TorsoRigGrp[0] )

# connect controls visibility attribute to the AllCtrl
cmds.connectAttr( AllCtrl+'.Show_Controls', TorsoRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', TorsoRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', TorsoRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Center_Color', TorsoRigGrp[0]+'.Ctrl_Color' )

print( '========================= made torso rig' )


# ---------------------------------------------------------------------------------------
# make Sluggy tail pivots

TailPivRet = denSR.den_makeTailPivs( prefix='', name='Tail', jointCount=8, radius=5 )
# capture all pivots in a variable
TailPivGrp = TailPivRet
# parent pivots under root pivot group
cmds.parent( TailPivGrp, RootPivGrp )

# position tail pivots
cmds.xform( 'Tail01_Piv', t=( 0.0, 119.52014336654541, -118.37164764355575 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'Tail02_Piv', t=( 0.0, 112.6407078190961, -165.33433306014513 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'Tail03_Piv', t=( 0.0, 111.20437116299254, -222.21161026868324 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'Tail04_Piv', t=( 0.0, 109.97711594117408, -277.93971238744916 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'Tail05_Piv', t=( 0.0, 109.01820146227057, -336.8335338539647 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'Tail06_Piv', t=( 0.0, 108.23519864274955, -393.2815444034674 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'Tail07_Piv', t=( 0.0, 108.22145235236398, -448.22708709896 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'Tail08_Piv', t=( 0.0, 108.39554250459224, -508.6147507816687 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'TailEnd_Piv', t=( 0.0, 107.37561547162288, -598.2196188438623 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )



# ---------------------------------------------------------------------------------------
# make Sluggy tail rig (for full IK/FK blendable tail)

TailRigRet = denSR.den_makeTailRig( prefix='', name='Tail', jointCount=8, radius=5, ctrlRadius=22.0, controlJoints=(1,4,8), dpTime=0.01  )
print( TailRigRet )

# capture the rig group in a variable
TailRigGrp = TailRigRet[0]; print( TailRigGrp )
# capture spaceIn, spaceOUT, BindJoints, Controls, and Guts in 5 variables
TailSpaceINs = TailRigRet[1]; print( TailSpaceINs )
TailSpaceOUTs = TailRigRet[2]; print( TailSpaceOUTs )
TailBindJnts = TailRigRet[3]; print( TailBindJnts )
TailCtrlsALL = TailRigRet[4]; print( TailCtrlsALL )
TailGutsALL = TailRigRet[5]; print( TailGutsALL )
TailHandles = TailRigRet[6]; print( TailHandles )
# make new variables for later connecting attributes
TailSpaceIN = TailSpaceINs[0]; print( TailSpaceIN )


# connect to geometry
denUt.den_connectBoxGeo( Jnts=TailBindJnts )
denUt.den_connectProxyGeo( Jnts=TailBindJnts )

# parent rig under root rig group
TailRigGrp = cmds.parent( TailRigGrp, RootRigGrp )

# Connect translate/rotate/scale of spaceINs to its spaceOUTs with constraint
cmds.parentConstraint( PelvisSpaceOUT, TailSpaceIN, mo=True )
cmds.scaleConstraint( PelvisSpaceOUT, TailSpaceIN, mo=True )


# ---------------------------------------------------------------------------------------
# make Sluggy tail rig dynamics (only works for IK or IK/FK-blendable tails, does not support FK tails)

TailDynRet = denSR.den_addTailDynamics( prefix='', name='Tail', TailRigGrp=TailRigGrp, TailSpaceIN=TailSpaceIN, TailHandles=TailHandles, TailBindJnts=TailBindJnts, dpTime=0.01 )
print( TailDynRet )

# capture the rig dynamics group in a variable
TailDynCtrl = TailDynRet[0]; print( TailDynCtrl )

# den - customize dynamics attributes here if necessary
cmds.setAttr( TailDynCtrl+'.stretchResistance', 100 )
cmds.setAttr( TailDynCtrl+'.compressionResistance', 100 )
cmds.setAttr( TailDynCtrl+'.bendResistance', 20 )
cmds.setAttr( TailDynCtrl+'.startCurveAttract', 0.01 )

# add safetycovers and etc.
denUt.den_AddSafetyCovers( rigGroup=TailRigGrp[0] )

# connect controls visibility attribute to the AllCtrl
cmds.connectAttr( AllCtrl+'.Show_Controls', TailRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', TailRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', TailRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Center_Color', TailRigGrp[0]+'.Ctrl_Color' )


# ---------------------------------------------------------------------------------------
# make Trex leg pivots

# create pivots for left side
L_TrexLegPivGrp = denTR.den_makeTrexHindLegPivs( side='L_', prefix='', name='TrexLeg', radius=5.0 )
# parent under root pivot group
L_TrexLegPivGrp = cmds.parent( L_TrexLegPivGrp, RootPivGrp )

# create pivots for right side
R_TrexLegPivGrp = denTR.den_makeTrexHindLegPivs( side='R_', prefix='', name='TrexLeg', radius=5.0 )
# parent under root pivot group
R_TrexLegPivGrp = cmds.parent( R_TrexLegPivGrp, RootPivGrp )

# position pivots for the Left -------
cmds.xform( 'L_TrexLegPiv_Grp|L_Heel_Piv', t=( 31.590957104254848, 0.0, -95.51288326694325 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
#cmds.xform( 'L_TrexLegPiv_Grp|L_Heel_Piv|L_FootUp_Piv', t=( -1.4832539041998274, 27.265602056526834, 12.323137449707488 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_TrexLegPiv_Grp|L_Heel_Piv|L_Ankle_Piv', t=( -1.1594670744284485, 17.67643623861909, -0.7251422678916981 ), ro=( 86.23123165620092, -40.49688492940294, -81.7139679457255 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_TrexLegPiv_Grp|L_Heel_Piv|L_Ball_Piv', t=( 0.9001808135587979, 3.533927548017509, 11.479779292496652 ), ro=( 7.096800525194601, 1.2601541368111406, 5.779700517616046 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_TrexLegPiv_Grp|L_Heel_Piv|L_BallSole_Piv', t=( 0.9001808135587979, 0.0, 11.479779292496652 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_TrexLegPiv_Grp|L_Heel_Piv|L_Toe_Piv', t=( 1.899999999999995, 0.0, 40.522165804925564 ), ro=( 7.096800525194602, 1.260154136811134, 5.779700517616045 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_TrexLegPiv_Grp|L_Heel_Piv|L_SoleLF_Piv', t=( 20.341600196209193, 0.0, 14.523387157568557 ), ro=( 23.51809344429739, 36.844573069301646, 35.96992974963205 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_TrexLegPiv_Grp|L_Heel_Piv|L_SoleLB_Piv', t=( 8.119419094810944, 0.0, 1.3222736240269626 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_TrexLegPiv_Grp|L_Heel_Piv|L_SoleRF_Piv', t=( -19.253397042412736, 0.0, 14.823387157568561 ), ro=( 12.666612408113016, -21.6522586782138, -31.346317204764958 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_TrexLegPiv_Grp|L_Heel_Piv|L_SoleRB_Piv', t=( -13.16359567527756, 0.0, 1.7222736240269683 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_TrexLegPiv_Grp|L_Hip_Piv', t=( 18.3538050865588, 126.9812159714599, -90.25431509006225 ), ro=( -105.20445071952413, -22.315625041627307, -73.96688487360498 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_TrexLegPiv_Grp|L_Knee_Piv', t=( 32.84999070146403, 76.53706315695416, -68.7116253059772 ), ro=( -113.22634422968868, 52.0318588548282, -98.55032076968094 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_TrexLegPiv_Grp|L_Hock_Piv', t=( 28.505752391339584, 47.6427017962836, -106.15327794812359 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_TrexLegPiv_Grp|L_Hock_Loc', t=( 28.505752391339584, 47.6427017962836, -106.15327794812359 ), ro=( 75.96561405097573, -18.27318989321547, -86.32302781362934 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_TrexLegPiv_Grp|L_KneeMid_Loc', t=( 24.3926475581926, 72.3288261050395, -93.2461703124486 ), ro=( 69.96661262399901, 3.1145179818207116, -83.69465307413763 ), s=( 1.0, 1.0, 1.0 ) )
#cmds.xform( 'L_TrexLegPiv_Grp|L_KneeMid_Loc|L_KneePole_Loc', t=( -12.794415272585155, 74.51383269849487, 0.0 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_TrexLegPiv_Grp|L_KneeMid2_Loc', t=( 23.429778738949192, 87.31195888387175, -98.20379651909292 ), ro=( 75.67813100856524, 11.242337748642761, -82.70820706969786 ), s=( 1.0, 1.0, 1.0 ) )
#cmds.xform( 'L_TrexLegPiv_Grp|L_KneeMid2_Loc|L_KneePole2_Loc', t=( -8.400938796190147, 79.13815577275452, 0.0 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_KneePole_Loc', t=( -50.9516788909797, 74.00970986534631, 0.0 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FootUp_Piv', t=( 2.3427919511020647, 30.058256931073974, 14.608036892518783 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_KneePole2_Loc', t=( -46.105330210240226, 73.57694032237605, 0.0 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )


# position pivots for the Right -------
cmds.xform( 'R_TrexLegPiv_Grp|R_Heel_Piv', t=( 31.590957104254848, 0.0, -95.51288326694325 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
#cmds.xform( 'R_TrexLegPiv_Grp|R_Heel_Piv|R_FootUp_Piv', t=( -1.4832539041998274, 27.265602056526834, 12.323137449707488 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_TrexLegPiv_Grp|R_Heel_Piv|R_Ankle_Piv', t=( -1.1594670744284485, 17.67643623861909, -0.7251422678916981 ), ro=( 86.23123165620092, -40.49688492940294, -81.7139679457255 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_TrexLegPiv_Grp|R_Heel_Piv|R_Ball_Piv', t=( 0.9001808135587979, 3.533927548017509, 11.479779292496652 ), ro=( 7.096800525194601, 1.2601541368111406, 5.779700517616046 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_TrexLegPiv_Grp|R_Heel_Piv|R_BallSole_Piv', t=( 0.9001808135587979, 0.0, 11.479779292496652 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_TrexLegPiv_Grp|R_Heel_Piv|R_Toe_Piv', t=( 1.899999999999995, 0.0, 40.522165804925564 ), ro=( 7.096800525194602, 1.260154136811134, 5.779700517616045 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_TrexLegPiv_Grp|R_Heel_Piv|R_SoleLF_Piv', t=( 20.341600196209193, 0.0, 14.523387157568557 ), ro=( 23.51809344429739, 36.844573069301646, 35.96992974963205 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_TrexLegPiv_Grp|R_Heel_Piv|R_SoleLB_Piv', t=( 8.119419094810944, 0.0, 1.3222736240269626 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_TrexLegPiv_Grp|R_Heel_Piv|R_SoleRF_Piv', t=( -19.253397042412736, 0.0, 14.823387157568561 ), ro=( 12.666612408113016, -21.6522586782138, -31.346317204764958 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_TrexLegPiv_Grp|R_Heel_Piv|R_SoleRB_Piv', t=( -13.16359567527756, 0.0, 1.7222736240269683 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_TrexLegPiv_Grp|R_Hip_Piv', t=( 18.3538050865588, 126.9812159714599, -90.25431509006225 ), ro=( -105.20445071952413, -22.315625041627307, -73.96688487360498 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_TrexLegPiv_Grp|R_Knee_Piv', t=( 32.84999070146403, 76.53706315695416, -68.7116253059772 ), ro=( -113.22634422968868, 52.0318588548282, -98.55032076968094 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_TrexLegPiv_Grp|R_Hock_Piv', t=( 28.505752391339584, 47.6427017962836, -106.15327794812359 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_TrexLegPiv_Grp|R_Hock_Loc', t=( 28.505752391339584, 47.6427017962836, -106.15327794812359 ), ro=( 75.96561405097573, -18.27318989321547, -86.32302781362934 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_TrexLegPiv_Grp|R_KneeMid_Loc', t=( 24.3926475581926, 72.3288261050395, -93.2461703124486 ), ro=( 69.96661262399901, 3.1145179818207116, -83.69465307413763 ), s=( 1.0, 1.0, 1.0 ) )
#cmds.xform( 'R_TrexLegPiv_Grp|R_KneeMid_Loc|R_KneePole_Loc', t=( -12.794415272585155, 74.51383269849487, 0.0 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_TrexLegPiv_Grp|R_KneeMid2_Loc', t=( 23.429778738949192, 87.31195888387175, -98.20379651909292 ), ro=( 75.67813100856524, 11.242337748642761, -82.70820706969786 ), s=( 1.0, 1.0, 1.0 ) )
#cmds.xform( 'R_TrexLegPiv_Grp|R_KneeMid2_Loc|R_KneePole2_Loc', t=( -8.400938796190147, 79.13815577275452, 0.0 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_KneePole_Loc', t=( -50.9516788909797, 74.00970986534631, 0.0 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FootUp_Piv', t=( 2.3427919511020647, 30.058256931073974, 14.608036892518783 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_KneePole2_Loc', t=( -46.105330210240226, 73.57694032237605, 0.0 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )


# dp refresh
denUt.den_DiagPause( seconds=0.01 )

######## ============================= LEG =========================================
# ---------------------------------------------------------------------------------------
# make Trex leg rig

# create rig for the Left -------
L_LegRigRet = denTR.den_makeTrexHindLegRig( side='L_', prefix='', name='TrexLeg', radius=5.0, ctrlRadius=15.0, displayLocalAxis=False )
print( L_LegRigRet )
# capture the rig group in a variable
L_LegRigGrp = L_LegRigRet[0]; print( L_LegRigGrp )
# capture spaceIn, spaceOUT, BindJoints, Controls, and Guts in 5 variables
L_LegSpaceINs = L_LegRigRet[1]; print( L_LegSpaceINs )
L_LegSpaceOUTs = L_LegRigRet[2]; print( L_LegSpaceOUTs )
L_LegBindJoints = L_LegRigRet[3]; print( L_LegBindJoints )
L_LegCtrlsALL = L_LegRigRet[4]; print( L_LegCtrlsALL )
L_LegGutsALL = L_LegRigRet[5]; print( L_LegGutsALL )
# make new variables for later connecting attributes
L_LegPelvisSpaceIN = L_LegSpaceINs[0]; print( L_LegPelvisSpaceIN )
L_LegCogSpaceIN = L_LegSpaceINs[1]; print( L_LegCogSpaceIN )
L_LegAllSpaceIN = L_LegSpaceINs[2]; print( L_LegAllSpaceIN )
L_AnkleSpaceOUT = L_LegSpaceOUTs[0]; print( L_AnkleSpaceOUT )

# connect geometry
denUt.den_connectBoxGeo( Jnts=L_LegBindJoints )
denUt.den_connectProxyGeo( Jnts=L_LegBindJoints )

# parent rig under root rig group
L_LegRigGrp = cmds.parent( L_LegRigGrp, RootRigGrp )

# Connect translate/rotate/scale of spaceINs to its spaceOUTs with constraint
cmds.parentConstraint( PelvisSpaceOUT, L_LegPelvisSpaceIN, mo=True )
cmds.parentConstraint( CogSpaceOUT, L_LegCogSpaceIN, mo=True )
cmds.parentConstraint( AllSpaceOUT, L_LegAllSpaceIN, mo=True )
cmds.scaleConstraint( PelvisSpaceOUT, L_LegPelvisSpaceIN, mo=True )
cmds.scaleConstraint( CogSpaceOUT, L_LegCogSpaceIN, mo=True )
cmds.scaleConstraint( AllSpaceOUT, L_LegAllSpaceIN, mo=True )


# create rig for the Right -------
R_LegRigRet = denTR.den_makeTrexHindLegRig( side='R_', prefix='', name='TrexLeg', radius=5.0, ctrlRadius=15.0, displayLocalAxis=False )
print( R_LegRigRet )
# capture the rig group in a variable
R_LegRigGrp = R_LegRigRet[0]; print( R_LegRigGrp )
# capture spaceIn, spaceOUT, BindJoints, Controls, and Guts in 5 variables
R_LegSpaceINs = R_LegRigRet[1]; print( R_LegSpaceINs )
R_LegSpaceOUTs = R_LegRigRet[2]; print( R_LegSpaceOUTs )
R_LegBindJoints = R_LegRigRet[3]; print( R_LegBindJoints )
R_LegCtrlsALL = R_LegRigRet[4]; print( R_LegCtrlsALL )
R_LegGutsALL = R_LegRigRet[5]; print( R_LegGutsALL )
# make new variables for later connecting attributes
R_LegPelvisSpaceIN = R_LegSpaceINs[0]; print( R_LegPelvisSpaceIN )
R_LegCogSpaceIN = R_LegSpaceINs[1]; print( R_LegCogSpaceIN )
R_LegAllSpaceIN = R_LegSpaceINs[2]; print( R_LegAllSpaceIN )
R_AnkleSpaceOUT = R_LegSpaceOUTs[0]; print( R_AnkleSpaceOUT )

# connect geometry
denUt.den_connectBoxGeo( Jnts=R_LegBindJoints )
denUt.den_connectProxyGeo( Jnts=R_LegBindJoints )

# parent rig under root rig group
R_LegRigGrp = cmds.parent( R_LegRigGrp, RootRigGrp )

# Connect translate/rotate/scale of spaceINs to its spaceOUTs with constraint
cmds.parentConstraint( PelvisSpaceOUT, R_LegPelvisSpaceIN, mo=True )
cmds.parentConstraint( CogSpaceOUT, R_LegCogSpaceIN, mo=True )
cmds.parentConstraint( AllSpaceOUT, R_LegAllSpaceIN, mo=True )
cmds.scaleConstraint( PelvisSpaceOUT, R_LegPelvisSpaceIN, mo=True )
cmds.scaleConstraint( CogSpaceOUT, R_LegCogSpaceIN, mo=True )
cmds.scaleConstraint( AllSpaceOUT, R_LegAllSpaceIN, mo=True )

######## -------------------------------------
# Add Left leg twist

L_LegTwistRigRet = denBR.den_makeTwists( side='L_', radius=1.997, Joints=['Hip','Knee','Hock'], ctrlPos=(0,0,10), ctrlUpVec=(0,0,1), displayLocalAxis=False )
print( L_LegTwistRigRet )
L_LegTwistBindJnts = L_LegTwistRigRet[3]; print( L_LegTwistBindJnts )
L_LegTwistCtrlsALL = L_LegTwistRigRet[4]; print( L_LegTwistCtrlsALL )

denUt.den_connectProxyGeo( Jnts=L_LegTwistBindJnts )


print('========================= made L_ leg twists')

######## -------------------------------------
# Add Right leg twist

R_LegTwistRigRet = denBR.den_makeTwists( side='R_', radius=1.997, Joints=['Hip','Knee','Hock'], ctrlPos=(0,0,10), ctrlUpVec=(0,0,1), displayLocalAxis=False )
print( R_LegTwistRigRet )
R_LegTwistBindJnts = R_LegTwistRigRet[3]; print( R_LegTwistBindJnts )
R_LegTwistCtrlsALL = R_LegTwistRigRet[4]; print( R_LegTwistCtrlsALL )

denUt.den_connectProxyGeo( Jnts=R_LegTwistBindJnts )


print('========================= made R_ leg twists')


denUt.den_AddSafetyCovers( rigGroup=L_LegRigGrp[0] )


# -------------------------------------
# For Left side leg
# add safetycovers and etc.
denUt.den_AddSafetyCovers( rigGroup=L_LegRigGrp[0] )

# connect controls visibility attribute to the AllCtrl
cmds.connectAttr( AllCtrl+'.Show_Controls', L_LegRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', L_LegRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', L_LegRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Left_Color', L_LegRigGrp[0]+'.Ctrl_Color' )


# -------------------------------------
# For Right side leg
# add safetycovers and etc.
denUt.den_AddSafetyCovers( rigGroup=R_LegRigGrp[0] )

# connect controls visibility attribute to the AllCtrl
cmds.connectAttr( AllCtrl+'.Show_Controls', R_LegRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', R_LegRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', R_LegRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Right_Color', R_LegRigGrp[0]+'.Ctrl_Color' )




######## ============================= TOE =========================================
# make Auto toe pivot

L_ToesPivGrp = denTR.den_makeToePivs( side='L_', name='Toe', toeList=['A','B','C','D'], numJnts=[4,4,4,4], radius=2.0, footPos=(5,0,-25) )
L_ToesPivGrp = cmds.parent( L_ToesPivGrp, RootPivGrp )

R_ToesPivGrp = denTR.den_makeToePivs( side='R_', name='Toe', toeList=['A','B','C','D'], numJnts=[4,4,4,4], radius=2.0, footPos=(-5,0,-25) )
R_ToesPivGrp = cmds.parent( R_ToesPivGrp, RootPivGrp )

# position pivots
cmds.xform( 'L_ToeC01_Piv', t=( 34.524125949256145, 18.072419727445926, -89.5724341993369 ), ro=( -102.34543207322302, -39.09490727388732, -78.74679138409948 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_ToeC03_Piv', t=( 38.288885847932896, 7.949515239157741, -75.2821296145143 ), ro=( -145.53489995075233, -76.7079946662288, -34.35287902631754 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_ToeB03_Piv', t=( 25.719018609374007, 7.543690508398209, -75.25202829797172 ), ro=( -55.62961815014626, -69.46618801625701, -120.94559029055029 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_ToeBUp_Piv', t=( 28.506400284598232, -2.2, -87.61785716146953 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_ToeCUp_Piv', t=( 36.05621765396205, -2.2, -87.61785716146953 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_ToeB01_Piv', t=( 28.312947568601498, 18.091858023746717, -88.18891995479838 ), ro=( -76.03527171532625, -36.33327991164371, -97.51559466728885 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_ToeDUp_Piv', t=( 42.38482313557765, -2.2, -87.61785716146953 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_ToeA04_Piv', t=( 14.950023618872367, 4.734776912808995, -79.2787786230796 ), ro=( -26.304718867338, -56.1709432989006, -143.17571516463755 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_ToeD01_Piv', t=( 38.909796192677305, 16.561667787362648, -92.68852028710664 ), ro=( -150.05308007421482, -26.605626300703864, -60.64978624785892 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_ToeD02_Piv', t=( 42.53128007365999, 10.121491006580019, -88.98769062722386 ), ro=( -156.67221011468936, -51.63258911947769, -33.915361763360515 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_ToeC04_Piv', t=( 39.95458080908284, 6.811001110947088, -66.74171182599507 ), ro=( -114.29940859112531, -61.213405494150365, -66.34607153281952 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_ToeD03_Piv', t=( 46.195120808688934, 7.6580660595481564, -83.41083842711623 ), ro=( -161.3765888809028, -48.5600254845182, -26.642613450690824 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_ToeA02_Piv', t=( 20.50463747529818, 10.125214294124051, -89.41618616103572 ), ro=( -37.36501422791061, -46.43369454747696, -127.95937909260296 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_ToeB02_Piv', t=( 27.33266659179482, 10.661513064579049, -82.67678833666095 ), ro=( -59.80465690208528, -64.69379384287781, -117.36409862814833 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_ToeBEnd_Piv', t=( 21.825446426825017, 0.8120832049768456, -55.50038259627322 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_ToeCEnd_Piv', t=( 42.582170457396, 0.8120832049768456, -54.82226408861681 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_ToeB04_Piv', t=( 24.091297167245045, 4.8288707470269525, -66.80100256138508 ), ro=( -57.654442715425276, -67.79957254238428, -119.42713814673037 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_ToeD04_Piv', t=( 49.115623828930005, 6.192869280743642, -79.70986801267507 ), ro=( -151.27015769727132, -43.36186082632599, -39.86742275785063 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_ToeDEnd_Piv', t=( 55.55841236804358, 0.8120832049768456, -71.7824572996848 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_ToeAEnd_Piv', t=( 9.711081589593247, 0.8120832049768456, -69.51303216717426 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_ToeAUp_Piv', t=( 20.51694663564505, -2.2, -87.61785716146953 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_ToeC02_Piv', t=( 36.20878233876675, 9.605558195001246, -82.557994870541 ), ro=( -137.56449945313167, -69.92619568907665, -38.524519823222704 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_ToeA03_Piv', t=( 16.84499087793105, 5.434228899160183, -83.16107453348339 ), ro=( -9.069892537901177, -62.51232331932453, -159.74037562551854 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_ToeA01_Piv', t=( 22.683780066625005, 16.455804225501264, -92.83916056822932 ), ro=( -42.61965449575911, -27.078925712499473, -108.99470544413221 ), s=( 1.0, 1.0, 1.0 ) )




cmds.xform( 'R_ToeC01_Piv', t=( 34.524125949256145, 18.072419727445926, -89.5724341993369 ), ro=( -102.34543207322302, -39.09490727388732, -78.74679138409948 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_ToeC03_Piv', t=( 38.288885847932896, 7.949515239157741, -75.2821296145143 ), ro=( -145.53489995075233, -76.7079946662288, -34.35287902631754 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_ToeB03_Piv', t=( 25.719018609374007, 7.543690508398209, -75.25202829797172 ), ro=( -55.62961815014626, -69.46618801625701, -120.94559029055029 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_ToeBUp_Piv', t=( 28.506400284598232, -2.2, -87.61785716146953 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_ToeCUp_Piv', t=( 36.05621765396205, -2.2, -87.61785716146953 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_ToeB01_Piv', t=( 28.312947568601498, 18.091858023746717, -88.18891995479838 ), ro=( -76.03527171532625, -36.33327991164371, -97.51559466728885 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_ToeDUp_Piv', t=( 42.38482313557765, -2.2, -87.61785716146953 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_ToeA04_Piv', t=( 14.950023618872367, 4.734776912808995, -79.2787786230796 ), ro=( -26.304718867338, -56.1709432989006, -143.17571516463755 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_ToeD01_Piv', t=( 38.909796192677305, 16.561667787362648, -92.68852028710664 ), ro=( -150.05308007421482, -26.605626300703864, -60.64978624785892 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_ToeD02_Piv', t=( 42.53128007365999, 10.121491006580019, -88.98769062722386 ), ro=( -156.67221011468936, -51.63258911947769, -33.915361763360515 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_ToeC04_Piv', t=( 39.95458080908284, 6.811001110947088, -66.74171182599507 ), ro=( -114.29940859112531, -61.213405494150365, -66.34607153281952 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_ToeD03_Piv', t=( 46.195120808688934, 7.6580660595481564, -83.41083842711623 ), ro=( -161.3765888809028, -48.5600254845182, -26.642613450690824 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_ToeA02_Piv', t=( 20.50463747529818, 10.125214294124051, -89.41618616103572 ), ro=( -37.36501422791061, -46.43369454747696, -127.95937909260296 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_ToeB02_Piv', t=( 27.33266659179482, 10.661513064579049, -82.67678833666095 ), ro=( -59.80465690208528, -64.69379384287781, -117.36409862814833 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_ToeBEnd_Piv', t=( 21.825446426825017, 0.8120832049768456, -55.50038259627322 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_ToeCEnd_Piv', t=( 42.582170457396, 0.8120832049768456, -54.82226408861681 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_ToeB04_Piv', t=( 24.091297167245045, 4.8288707470269525, -66.80100256138508 ), ro=( -57.654442715425276, -67.79957254238428, -119.42713814673037 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_ToeD04_Piv', t=( 49.115623828930005, 6.192869280743642, -79.70986801267507 ), ro=( -151.27015769727132, -43.36186082632599, -39.86742275785063 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_ToeDEnd_Piv', t=( 55.55841236804358, 0.8120832049768456, -71.7824572996848 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_ToeAEnd_Piv', t=( 9.711081589593247, 0.8120832049768456, -69.51303216717426 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_ToeAUp_Piv', t=( 20.51694663564505, -2.2, -87.61785716146953 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_ToeC02_Piv', t=( 36.20878233876675, 9.605558195001246, -82.557994870541 ), ro=( -137.56449945313167, -69.92619568907665, -38.524519823222704 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_ToeA03_Piv', t=( 16.84499087793105, 5.434228899160183, -83.16107453348339 ), ro=( -9.069892537901177, -62.51232331932453, -159.74037562551854 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_ToeA01_Piv', t=( 22.683780066625005, 16.455804225501264, -92.83916056822932 ), ro=( -42.61965449575911, -27.078925712499473, -108.99470544413221 ), s=( 1.0, 1.0, 1.0 ) )




# ---------------------------------------------------------------------------------------
# make Auto toe rig

# create left toe rig
L_ToeRigRet = denTR.den_makeToeRig(side='L_', name='Toe', toeList=['A','B','C','D'], radius=3, doIK=True )
print( L_ToeRigRet )
L_ToeRigGrp = L_ToeRigRet[0]; print( L_ToeRigGrp )
L_ToeSpaceINs = L_ToeRigRet[1]; print( L_ToeSpaceINs )
L_ToeSpaceOUTs = L_ToeRigRet[2]; print( L_ToeSpaceOUTs )
L_ToeBindJnts = L_ToeRigRet[3]; print( L_ToeBindJnts )
L_ToeCtrlsALL = L_ToeRigRet[4]; print( L_ToeCtrlsALL )
L_ToeGutsALL = L_ToeRigRet[5]; print( L_ToeGutsALL )

denUt.den_connectProxyGeo( Jnts=L_ToeBindJnts )


L_ToesSpaceIN = L_ToeSpaceINs[0]

L_ToeRigGrp = cmds.parent( L_ToeRigGrp, RootRigGrp )

cmds.parentConstraint( L_AnkleSpaceOUT, L_ToesSpaceIN, mo=True )
cmds.scaleConstraint( L_AnkleSpaceOUT, L_ToesSpaceIN, mo=True )

# create right toe rig
R_ToeRigRet = denTR.den_makeToeRig(side='R_', name='Toe', toeList=['A','B','C','D'], radius=3, doIK=True )
print( R_ToeRigRet )
R_ToeRigGrp = R_ToeRigRet[0]; print( R_ToeRigGrp )
R_ToeSpaceINs = R_ToeRigRet[1]; print( R_ToeSpaceINs )
R_ToeSpaceOUTs = R_ToeRigRet[2]; print( R_ToeSpaceOUTs )
R_ToeBindJnts = R_ToeRigRet[3]; print( R_ToeBindJnts )
R_ToeCtrlsALL = R_ToeRigRet[4]; print( R_ToeCtrlsALL )
R_ToeGutsALL = R_ToeRigRet[5]; print( R_ToeGutsALL )

denUt.den_connectProxyGeo( Jnts=R_ToeBindJnts )


R_ToesSpaceIN = R_ToeSpaceINs[0]

R_ToeRigGrp = cmds.parent( R_ToeRigGrp, RootRigGrp )

cmds.parentConstraint( R_AnkleSpaceOUT, R_ToesSpaceIN, mo=True )
cmds.scaleConstraint( R_AnkleSpaceOUT, R_ToesSpaceIN, mo=True )


# set toe ik
# L
ballToeZeros = [ 'L_ToeA01IK_CtrlZero', 'L_ToeD01IK_CtrlZero', ]
for ballToeZero in ballToeZeros:
    print( ballToeZero )
    cmds.parentConstraint( 'L_Ball_Jnt', ballToeZero, mo=True )

# edit here to customize number of digits and fingers
toeToeZeros = [ 'L_ToeA02IK_CtrlZero', 'L_ToeA03IK_CtrlZero', 'L_ToeA04IK_CtrlZero' ]
toeToeZeros += [ 'L_ToeB01IK_CtrlZero', 'L_ToeB02IK_CtrlZero', 'L_ToeB03IK_CtrlZero', 'L_ToeB04IK_CtrlZero' ]
toeToeZeros += [ 'L_ToeC01IK_CtrlZero', 'L_ToeC02IK_CtrlZero', 'L_ToeC03IK_CtrlZero', 'L_ToeC04IK_CtrlZero' ]
toeToeZeros += [ 'L_ToeD02IK_CtrlZero', 'L_ToeD03IK_CtrlZero', 'L_ToeD04IK_CtrlZero' ]

for toeToeZero in toeToeZeros:
    print( toeToeZero )
    cmds.parentConstraint( 'L_Toe_Jnt', toeToeZero, mo=True )


# R
ballToeZeros = [ 'R_ToeA01IK_CtrlZero', 'R_ToeD01IK_CtrlZero', ]
for ballToeZero in ballToeZeros:
    print( ballToeZero )
    cmds.parentConstraint( 'R_Ball_Jnt', ballToeZero, mo=True )

toeToeZeros = [ 'R_ToeA02IK_CtrlZero', 'R_ToeA03IK_CtrlZero', 'R_ToeA04IK_CtrlZero' ]
toeToeZeros += [ 'R_ToeB01IK_CtrlZero', 'R_ToeB02IK_CtrlZero', 'R_ToeB03IK_CtrlZero', 'R_ToeB04IK_CtrlZero' ]
toeToeZeros += [ 'R_ToeC01IK_CtrlZero', 'R_ToeC02IK_CtrlZero', 'R_ToeC03IK_CtrlZero', 'R_ToeC04IK_CtrlZero' ]
toeToeZeros += [ 'R_ToeD02IK_CtrlZero', 'R_ToeD03IK_CtrlZero', 'R_ToeD04IK_CtrlZero' ]

for toeToeZero in toeToeZeros:
    print( toeToeZero )
    cmds.parentConstraint( 'R_Toe_Jnt', toeToeZero, mo=True )

# clean up
denUt.den_AddSafetyCovers( rigGroup=L_ToeRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', L_ToeRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', L_ToeRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', L_ToeRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Left_Color', L_ToeRigGrp[0]+'.Ctrl_Color' )


denUt.den_AddSafetyCovers( rigGroup=R_ToeRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', R_ToeRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', R_ToeRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', R_ToeRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Right_Color', R_ToeRigGrp[0]+'.Ctrl_Color' )




######## ============================= ARM =========================================
# ---------------------------------------------------------------------------------------
# make dog front leg pivots

# create pivots for Left side -------
L_DogFrontLegPivGrp = denAR.den_makeDogFrontLegPivs( side='L_', name='DogFrontLeg', radius=5.0 )

# parent under root pivot group
L_DogLegPivGrp = cmds.parent( L_DogFrontLegPivGrp, RootPivGrp )

# positon pivots for the left side
cmds.xform( 'L_Scap01_Piv', t=( -23.05732375932051, 130.89010001165656, 36.08478565090147 ), ro=( 148.3146465873851, 0.5530146745181408, 33.6807928872097 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_Scap02_Piv', t=( 16.840690154676086, 157.47944814561865, 35.62199737317914 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_Shld_Piv', t=( 31.642331973141836, 119.73322561549885, 60.161269730905595 ), ro=( 88.95020217713811, 38.9345124908079, -90.28882931470312 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_Elbow_Piv', t=( 31.467683308166073, 85.08803508726216, 32.171296607997476 ), ro=( 89.08334094074453, -27.021929004735174, -89.21256311562817 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_Fknee_Piv', t=( 32.267683308166085, 26.881798361276616, 61.85972580477241 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_Fknee_Loc', t=( 32.267683308166085, 26.881798361276616, 61.85972580477241 ), ro=( -96.84477490281188, -38.7387440468294, -93.36052443213767 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FlegMid_Loc', t=( 31.64691599807063, 68.06068082014349, 65.22708115513721 ), ro=( -90.32598229911568, -5.599202755905982, -89.99491712123036 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_ElbowPole_Loc', t=( -17.052047750335174, 84.98563051303907, 0.0 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FlegMid2_Loc', t=( 31.95500764065396, 73.30751198838773, 61.010497767839 ), ro=( -90.81671928266155, -1.0479247285363433, -89.61412062757547 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_ElbowPole2_Loc', t=( -4.936814134107493, 81.95200092638689, 0.0 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_Fheel_Piv', t=( 31.551500022999413, 0.0, 66.35393069657273 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FfootUp_Piv', t=( 7.105427357601002e-15, 25.570446942786766, 14.747710705407556 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_Fankle_Piv', t=( 0.1000000000000103, 16.388136024788118, 3.938961882796093 ), ro=( 90.11795415969831, -12.530487493027556, -89.53716806081687 ), s=( 1.0000000000000002, 1.0, 1.0000000000000002 ) )
cmds.xform( 'L_Fball_Piv', t=( 0.20000000000001883, 4.0090134072527235, 6.690348640839538 ), ro=( 6.7065753647667545, 0.5833402404651622, 0.7494391463244281 ), s=( 1.0, 0.9999999999999999, 1.0 ) )
cmds.xform( 'L_FballSole_Piv', t=( 0.20000000000001883, 0.0, 6.690348640839538 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_Ftoe_Piv', t=( 0.5999999999999996, 0.0, 40.82349422526635 ), ro=( 6.706575364766759, 0.5833402404651025, 0.7494391463249344 ), s=( 1.0, 1.0, 0.9999999999999999 ) )
cmds.xform( 'L_FsoleLF_Piv', t=( 16.155821244223038, 0.0, 20.68885068686869 ), ro=( 8.333420953559658, 15.174258282642835, 29.231637189924104 ), s=( 1.0, 0.9999999999999999, 1.0 ) )
cmds.xform( 'L_FsoleLB_Piv', t=( 12.18429232655319, 0.0, 7.910028392694059 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FsoleRF_Piv', t=( -13.75126288390755, 0.0, 20.78885068686869 ), ro=( 7.031992659914422, -15.34015121761024, -24.998258071196645 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FsoleRB_Piv', t=( -9.913675080946428, 0.0, 8.110028392694055 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )



# create pivots for Right side -------
R_DogFrontLegPivGrp = denAR.den_makeDogFrontLegPivs( side='R_', name='DogFrontLeg', radius=5.0 )
# parent under root pivot group
R_DogLegPivGrp = cmds.parent( R_DogFrontLegPivGrp, RootPivGrp )

# positon pivots for the right side
cmds.xform( 'R_Scap01_Piv', t=( -23.05732375932051, 130.89010001165656, 36.08478565090147 ), ro=( 148.3146465873851, 0.5530146745181408, 33.6807928872097 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_Scap02_Piv', t=( 16.840690154676086, 157.47944814561865, 35.62199737317914 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_Shld_Piv', t=( 31.642331973141836, 119.73322561549885, 60.161269730905595 ), ro=( 88.95020217713811, 38.9345124908079, -90.28882931470312 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_Elbow_Piv', t=( 31.467683308166073, 85.08803508726216, 32.171296607997476 ), ro=( 89.08334094074453, -27.021929004735174, -89.21256311562817 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_Fknee_Piv', t=( 32.267683308166085, 26.881798361276616, 61.85972580477241 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_Fknee_Loc', t=( 32.267683308166085, 26.881798361276616, 61.85972580477241 ), ro=( -96.84477490281188, -38.7387440468294, -93.36052443213767 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FlegMid_Loc', t=( 31.64691599807063, 68.06068082014349, 65.22708115513721 ), ro=( -90.32598229911568, -5.599202755905982, -89.99491712123036 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_ElbowPole_Loc', t=( -17.052047750335174, 84.98563051303907, 0.0 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FlegMid2_Loc', t=( 31.95500764065396, 73.30751198838773, 61.010497767839 ), ro=( -90.81671928266155, -1.0479247285363433, -89.61412062757547 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_ElbowPole2_Loc', t=( -4.936814134107493, 81.95200092638689, 0.0 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_Fheel_Piv', t=( 31.551500022999413, 0.0, 66.35393069657273 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FfootUp_Piv', t=( 7.105427357601002e-15, 25.570446942786766, 14.747710705407556 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_Fankle_Piv', t=( 0.1000000000000103, 16.388136024788118, 3.938961882796093 ), ro=( 90.11795415969831, -12.530487493027556, -89.53716806081687 ), s=( 1.0000000000000002, 1.0, 1.0000000000000002 ) )
cmds.xform( 'R_Fball_Piv', t=( 0.20000000000001883, 4.0090134072527235, 6.690348640839538 ), ro=( 6.7065753647667545, 0.5833402404651622, 0.7494391463244281 ), s=( 1.0, 0.9999999999999999, 1.0 ) )
cmds.xform( 'R_FballSole_Piv', t=( 0.20000000000001883, 0.0, 6.690348640839538 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_Ftoe_Piv', t=( 0.5999999999999996, 0.0, 40.82349422526635 ), ro=( 6.706575364766759, 0.5833402404651025, 0.7494391463249344 ), s=( 1.0, 1.0, 0.9999999999999999 ) )
cmds.xform( 'R_FsoleLF_Piv', t=( 16.155821244223038, 0.0, 20.68885068686869 ), ro=( 8.333420953559658, 15.174258282642835, 29.231637189924104 ), s=( 1.0, 0.9999999999999999, 1.0 ) )
cmds.xform( 'R_FsoleLB_Piv', t=( 12.18429232655319, 0.0, 7.910028392694059 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FsoleRF_Piv', t=( -13.75126288390755, 0.0, 20.78885068686869 ), ro=( 7.031992659914422, -15.34015121761024, -24.998258071196645 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FsoleRB_Piv', t=( -9.913675080946428, 0.0, 8.110028392694055 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )

# dp refresh
denUt.den_DiagPause( seconds=0.01 )


# ---------------------------------------------------------------------------------------
# make dog front leg rig


# make Left side rig -------
L_FlegRigRet = denAR.den_makeDogFrontLegRig( side='L_', name='DogFrontLeg', radius=5.0, ctrlRadius=15.0, displayLocalAxis=False )
print( L_FlegRigRet )
# capture the rig group in a variable
L_FlegRigGrp = L_FlegRigRet[0]; print( L_FlegRigGrp )
# capture spaceIn, spaceOUT, BindJoints, Controls, and Guts in 5 variables
L_FlegSpaceINs = L_FlegRigRet[1]; print( L_FlegSpaceINs )
L_FlegSpaceOUTs = L_FlegRigRet[2]; print( L_FlegSpaceOUTs )
L_FlegBindJnts = L_FlegRigRet[3]; print( L_FlegBindJnts )
L_FlegCtrlsALL = L_FlegRigRet[4]; print( L_FlegCtrlsALL )
L_FlegGutsALL = L_FlegRigRet[5]; print( L_FlegGutsALL )
# make new variables for later connecting attributes
L_FlegChestSpaceIN = L_FlegSpaceINs[0]; print( L_FlegChestSpaceIN )
L_FlegCogSpaceIN = L_FlegSpaceINs[1]; print( L_FlegCogSpaceIN )
L_FlegAllSpaceIN = L_FlegSpaceINs[2]; print( L_FlegAllSpaceIN )
L_AnkleSpaceOUT = L_FlegSpaceOUTs[0]; print( L_AnkleSpaceOUT )

# connect box/proxy geo
denUt.den_connectBoxGeo( Jnts=L_FlegBindJnts )
denUt.den_connectProxyGeo( Jnts=L_FlegBindJnts )
#denUt.den_makeBindJoints( JxJnts=L_FlegJxJoints )

# parent rig under root rig group
L_FlegRigGrp = cmds.parent( L_FlegRigGrp, RootRigGrp )

# Connect translate/rotate/scale of spaceINs to its spaceOUTs with constraint
cmds.parentConstraint( ChestSpaceOUT, L_FlegChestSpaceIN, mo=True )
cmds.parentConstraint( CogSpaceOUT, L_FlegCogSpaceIN, mo=True )
cmds.parentConstraint( AllSpaceOUT, L_FlegAllSpaceIN, mo=True )
cmds.scaleConstraint( ChestSpaceOUT, L_FlegChestSpaceIN, mo=True )
cmds.scaleConstraint( CogSpaceOUT, L_FlegCogSpaceIN, mo=True )
cmds.scaleConstraint( AllSpaceOUT, L_FlegAllSpaceIN, mo=True )


# make Right side rig -------
R_FlegRigRet = denAR.den_makeDogFrontLegRig( side='R_', name='DogFrontLeg', radius=5.0, ctrlRadius=15.0, displayLocalAxis=False )
print( R_FlegRigRet )
# capture the rig group in a variable
R_FlegRigGrp = R_FlegRigRet[0]; print( R_FlegRigGrp )
# capture spaceIn, spaceOUT, BindJoints, Controls, and Guts in 5 variables
R_FlegSpaceINs = R_FlegRigRet[1]; print( R_FlegSpaceINs )
R_FlegSpaceOUTs = R_FlegRigRet[2]; print( R_FlegSpaceOUTs )
R_FlegBindJnts = R_FlegRigRet[3]; print( R_FlegBindJnts )
R_FlegCtrlsALL = R_FlegRigRet[4]; print( R_FlegCtrlsALL )
R_FlegGutsALL = R_FlegRigRet[5]; print( R_FlegGutsALL )
# make new variables for later connecting attributes
R_FlegChestSpaceIN = R_FlegSpaceINs[0]; print( R_FlegChestSpaceIN )
R_FlegCogSpaceIN = R_FlegSpaceINs[1]; print( R_FlegCogSpaceIN )
R_FlegAllSpaceIN = R_FlegSpaceINs[2]; print( R_FlegAllSpaceIN )
R_AnkleSpaceOUT = R_FlegSpaceOUTs[0]; print( R_AnkleSpaceOUT )

# connect box/proxy geo
denUt.den_connectBoxGeo( Jnts=R_FlegBindJnts )
denUt.den_connectProxyGeo( Jnts=R_FlegBindJnts )

# parent rig under root rig group
R_FlegRigGrp = cmds.parent( R_FlegRigGrp, RootRigGrp )

# Connect translate/rotate/scale of spaceINs to its spaceOUTs with constraint
cmds.parentConstraint( ChestSpaceOUT, R_FlegChestSpaceIN, mo=True )
cmds.parentConstraint( CogSpaceOUT, R_FlegCogSpaceIN, mo=True )
cmds.parentConstraint( AllSpaceOUT, R_FlegAllSpaceIN, mo=True )
cmds.scaleConstraint( ChestSpaceOUT, R_FlegChestSpaceIN, mo=True )
cmds.scaleConstraint( CogSpaceOUT, R_FlegCogSpaceIN, mo=True )
cmds.scaleConstraint( AllSpaceOUT, R_FlegAllSpaceIN, mo=True )

############ -----------------------------
# add twist to front legs

L_LegTwistRigRet = denBR.den_makeTwists( side='L_', radius=1.997, Joints=['Shld','Elbow','Fknee'], ctrlPos=(0,0,10), ctrlUpVec=(0,0,1), displayLocalAxis=False )
print( L_LegTwistRigRet )
L_LegTwistBindJnts = L_LegTwistRigRet[3]; print( L_LegTwistBindJnts )
L_LegTwistCtrlsALL = L_LegTwistRigRet[4]; print( L_LegTwistCtrlsALL )

denUt.den_connectProxyGeo( Jnts=L_LegTwistBindJnts )


print('========================= made L_ leg twists')


R_LegTwistRigRet = denBR.den_makeTwists( side='R_', radius=1.997, Joints=['Shld','Elbow','Fknee'], ctrlPos=(0,0,10), ctrlUpVec=(0,0,1), displayLocalAxis=False )
print( R_LegTwistRigRet )
R_LegTwistBindJnts = R_LegTwistRigRet[3]; print( R_LegTwistBindJnts )
R_LegTwistCtrlsALL = R_LegTwistRigRet[4]; print( R_LegTwistCtrlsALL )

denUt.den_connectProxyGeo( Jnts=R_LegTwistBindJnts )


print('========================= made R_ leg twists')



# ---------------------------------------
# For Left side:
# add safty covers and etc.
denUt.den_AddSafetyCovers( rigGroup=L_FlegRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', L_FlegRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', L_FlegRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', L_FlegRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Left_Color', L_FlegRigGrp[0]+'.Ctrl_Color' )

# ---------------------------------------
# For Right side:
# add safty covers and etc.
denUt.den_AddSafetyCovers( rigGroup=R_FlegRigGrp[0] )

# connect controls visibility attribute to the AllCtrl
cmds.connectAttr( AllCtrl+'.Show_Controls', R_FlegRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', R_FlegRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', R_FlegRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Right_Color', R_FlegRigGrp[0]+'.Ctrl_Color' )




######## ============================= HAND =========================================
############ ---------------------------------------------------------------------------------------
# make fingers pivots using auto toe piv

L_FtoesPivGrp = denTR.den_makeToePivs( side='L_', name='Ftoe', toeList=['A','B','C','D','E'], numJnts=[3,4,4,4,4], radius=3, footPos=(5,0,25) )
L_FtoesPivGrp = cmds.parent( L_FtoesPivGrp, RootPivGrp )

R_FtoesPivGrp = denTR.den_makeToePivs( side='R_', name='Ftoe', toeList=['A','B','C','D','E'], numJnts=[3,4,4,4,4], radius=3, footPos=(-5,0,25) )
R_FtoesPivGrp = cmds.parent( R_FtoesPivGrp, RootPivGrp )

# positon pivots
cmds.xform( 'L_FtoeCEnd_Piv', t=( 32.07742871719934, 0.7823326178889953, 107.28042313561052 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FtoeE04_Piv', t=( 53.667804036404945, 5.9993153695115815, 78.93190876840413 ), ro=( -161.72038853735236, -26.368114717580728, -33.973533063782476 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FtoeE01_Piv', t=( 38.66160515291882, 16.294174823153416, 69.82430305812629 ), ro=( -152.53056346909895, -15.906059525793843, -59.63706905826391 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FtoeC03_Piv', t=( 31.724243451012292, 6.323927979147568, 86.66700278508155 ), ro=( -82.69194015615568, -86.6894565453653, -91.54711270446461 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FtoeDUp_Piv', t=( 26.51355129382444, 1.1145753595130596, 58.15770332776289 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FtoeAEnd_Piv', t=( 4.329639854931546, 0.8021928584508986, 76.06412096781297 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FtoeE03_Piv', t=( 48.90736975500165, 6.364761523490975, 75.96019168118949 ), ro=( -178.32006581751833, -31.899043308793797, -4.3898379834630665 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FtoeC01_Piv', t=( 31.779812496476815, 17.695652985135844, 74.17308211181766 ), ro=( -88.3977665961385, -30.573341296400837, -89.80051676094448 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FtoeA03_Piv', t=( 12.882334528903773, 6.155480358942885, 71.85011399554388 ), ro=( -2.245019222540881, -22.6676431923011, -147.95680004354634 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FtoeCUp_Piv', t=( 32.45918161437879, 1.1145753595130596, 58.15770332776289 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FtoeEUp_Piv', t=( 20.231791125457526, 1.1145753595130596, 58.15770332776289 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FtoeA02_Piv', t=( 18.511430927894388, 7.580220322840763, 69.53919620785591 ), ro=( 2.961577570627197, -21.701625054958352, -165.79656013885153 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FtoeEEnd_Piv', t=( 61.41001117363492, 0.7823326178889953, 83.5598066046794 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FtoeC04_Piv', t=( 31.712074095496323, 5.8733575455547395, 94.45921368865541 ), ro=( -88.70430311841278, -68.29252029224952, -85.89523674094654 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FtoeAUp_Piv', t=( 51.72866415651828, 1.1145753595130596, 58.15770332776289 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FtoeB01_Piv', t=( 26.782676696777344, 17.74057453132212, 72.59727992894948 ), ro=( -49.52824098796565, -28.643887680557988, -105.44094259118447 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FtoeD02_Piv', t=( 39.24318312806879, 9.743004051008871, 78.36542499930695 ), ro=( -146.62199699244235, -50.51488620615255, -40.92598683661638 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FtoeBUp_Piv', t=( 38.84508928351179, 1.1145753595130596, 58.15770332776289 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FtoeD03_Piv', t=( 42.795957895420976, 6.662672418232919, 84.07266592767932 ), ro=( -167.80314621047876, -56.52006996749366, -11.017495186335639 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FtoeC02_Piv', t=( 31.807968508688596, 9.608687098175043, 78.95065201822807 ), ro=( -86.88580445589153, -66.93441401149389, -91.46009305600761 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FtoeD04_Piv', t=( 46.87434030824717, 5.868622725794284, 90.35491050159673 ), ro=( -147.792627859485, -51.204078115201966, -41.48084910102182 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FtoeB04_Piv', t=( 16.038227702703395, 5.921740582236335, 88.62164083421492 ), ro=( -31.078962445037103, -45.10726643994971, -144.14631688865356 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FtoeBEnd_Piv', t=( 8.926317322992627, 0.7823326178889953, 97.42911027920057 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FtoeB02_Piv', t=( 24.603386244089563, 9.850736157184405, 77.0681780254214 ), ro=( -29.76383210734208, -46.51459775190904, -140.75269936559977 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FtoeDEnd_Piv', t=( 52.627218956403915, 0.7823326178889953, 99.9069649147779 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FtoeA01_Piv', t=( 24.529306420027197, 15.743797347247849, 67.25460128770811 ), ro=( -14.515074538455634, -12.694685332617462, -126.39621416219849 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FtoeB03_Piv', t=( 19.82769116654285, 5.949204793568423, 83.56992796841735 ), ro=( -0.7486463968586735, -53.12445299161956, -179.58475497620285 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FtoeE02_Piv', t=( 42.58212443017193, 9.601895126308289, 72.03457297227472 ), ro=( -166.08424460287114, -28.919688209228624, -27.102455278735224 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FtoeD01_Piv', t=( 36.4455469454202, 16.725960185053225, 72.86996355822707 ), ro=( -129.46591597256668, -36.149389360925866, -68.16709464635865 ), s=( 1.0, 1.0, 1.0 ) )





cmds.xform( 'R_FtoeCEnd_Piv', t=( 32.07742871719934, 0.7823326178889953, 107.28042313561052 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FtoeE04_Piv', t=( 53.667804036404945, 5.9993153695115815, 78.93190876840413 ), ro=( -161.72038853735236, -26.368114717580728, -33.973533063782476 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FtoeE01_Piv', t=( 38.66160515291882, 16.294174823153416, 69.82430305812629 ), ro=( -152.53056346909895, -15.906059525793843, -59.63706905826391 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FtoeC03_Piv', t=( 31.724243451012292, 6.323927979147568, 86.66700278508155 ), ro=( -82.69194015615568, -86.6894565453653, -91.54711270446461 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FtoeDUp_Piv', t=( 26.51355129382444, 1.1145753595130596, 58.15770332776289 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FtoeAEnd_Piv', t=( 4.329639854931546, 0.8021928584508986, 76.06412096781297 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FtoeE03_Piv', t=( 48.90736975500165, 6.364761523490975, 75.96019168118949 ), ro=( -178.32006581751833, -31.899043308793797, -4.3898379834630665 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FtoeC01_Piv', t=( 31.779812496476815, 17.695652985135844, 74.17308211181766 ), ro=( -88.3977665961385, -30.573341296400837, -89.80051676094448 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FtoeA03_Piv', t=( 12.882334528903773, 6.155480358942885, 71.85011399554388 ), ro=( -2.245019222540881, -22.6676431923011, -147.95680004354634 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FtoeCUp_Piv', t=( 32.45918161437879, 1.1145753595130596, 58.15770332776289 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FtoeEUp_Piv', t=( 20.231791125457526, 1.1145753595130596, 58.15770332776289 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FtoeA02_Piv', t=( 18.511430927894388, 7.580220322840763, 69.53919620785591 ), ro=( 2.961577570627197, -21.701625054958352, -165.79656013885153 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FtoeEEnd_Piv', t=( 61.41001117363492, 0.7823326178889953, 83.5598066046794 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FtoeC04_Piv', t=( 31.712074095496323, 5.8733575455547395, 94.45921368865541 ), ro=( -88.70430311841278, -68.29252029224952, -85.89523674094654 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FtoeAUp_Piv', t=( 51.72866415651828, 1.1145753595130596, 58.15770332776289 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FtoeB01_Piv', t=( 26.782676696777344, 17.74057453132212, 72.59727992894948 ), ro=( -49.52824098796565, -28.643887680557988, -105.44094259118447 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FtoeD02_Piv', t=( 39.24318312806879, 9.743004051008871, 78.36542499930695 ), ro=( -146.62199699244235, -50.51488620615255, -40.92598683661638 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FtoeBUp_Piv', t=( 38.84508928351179, 1.1145753595130596, 58.15770332776289 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FtoeD03_Piv', t=( 42.795957895420976, 6.662672418232919, 84.07266592767932 ), ro=( -167.80314621047876, -56.52006996749366, -11.017495186335639 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FtoeC02_Piv', t=( 31.807968508688596, 9.608687098175043, 78.95065201822807 ), ro=( -86.88580445589153, -66.93441401149389, -91.46009305600761 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FtoeD04_Piv', t=( 46.87434030824717, 5.868622725794284, 90.35491050159673 ), ro=( -147.792627859485, -51.204078115201966, -41.48084910102182 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FtoeB04_Piv', t=( 16.038227702703395, 5.921740582236335, 88.62164083421492 ), ro=( -31.078962445037103, -45.10726643994971, -144.14631688865356 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FtoeBEnd_Piv', t=( 8.926317322992627, 0.7823326178889953, 97.42911027920057 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FtoeB02_Piv', t=( 24.603386244089563, 9.850736157184405, 77.0681780254214 ), ro=( -29.76383210734208, -46.51459775190904, -140.75269936559977 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FtoeDEnd_Piv', t=( 52.627218956403915, 0.7823326178889953, 99.9069649147779 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FtoeA01_Piv', t=( 24.529306420027197, 15.743797347247849, 67.25460128770811 ), ro=( -14.515074538455634, -12.694685332617462, -126.39621416219849 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FtoeB03_Piv', t=( 19.82769116654285, 5.949204793568423, 83.56992796841735 ), ro=( -0.7486463968586735, -53.12445299161956, -179.58475497620285 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FtoeE02_Piv', t=( 42.58212443017193, 9.601895126308289, 72.03457297227472 ), ro=( -166.08424460287114, -28.919688209228624, -27.102455278735224 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FtoeD01_Piv', t=( 36.4455469454202, 16.725960185053225, 72.86996355822707 ), ro=( -129.46591597256668, -36.149389360925866, -68.16709464635865 ), s=( 1.0, 1.0, 1.0 ) )



# ---------------------------------------------------------------------------------------
# make finger rig using Auto toe rig 
# L
L_FtoeRigRet = denTR.den_makeToeRig(side='L_', name='Ftoe', toeList=['A','B','C','D','E'], radius=2, doIK=True )
print( L_FtoeRigRet )
L_FtoeRigGrp = L_FtoeRigRet[0]; print( L_FtoeRigGrp )
L_FtoeSpaceINs = L_FtoeRigRet[1]; print( L_FtoeSpaceINs )
L_FtoeSpaceOUTs = L_FtoeRigRet[2]; print( L_FtoeSpaceOUTs )
L_FtoeBindJnts = L_FtoeRigRet[3]; print( L_FtoeBindJnts )
L_FtoeCtrlsALL = L_FtoeRigRet[4]; print( L_FtoeCtrlsALL )
L_FtoeGutsALL = L_FtoeRigRet[5]; print( L_FtoeGutsALL )

denUt.den_connectProxyGeo( Jnts=L_FtoeBindJnts )


L_FtoesSpaceIN = L_FtoeSpaceINs[0]

L_FtoeRigGrp = cmds.parent( L_FtoeRigGrp, RootRigGrp )

cmds.parentConstraint( L_AnkleSpaceOUT, L_FtoesSpaceIN )
cmds.scaleConstraint( L_AnkleSpaceOUT, L_FtoesSpaceIN )

# set ik for fingers
ballToeZeros = [ 'L_FtoeA01IK_CtrlZero', 'L_FtoeE01IK_CtrlZero', ]
for ballToeZero in ballToeZeros:
    print( ballToeZero )
    cmds.parentConstraint( 'L_Fball_Jnt', ballToeZero, mo=True )

toeToeZeros = [ 'L_FtoeA02IK_CtrlZero', 'L_FtoeA03IK_CtrlZero' ]
toeToeZeros += [ 'L_FtoeB01IK_CtrlZero', 'L_FtoeB02IK_CtrlZero', 'L_FtoeB03IK_CtrlZero', 'L_FtoeB04IK_CtrlZero' ]
toeToeZeros += [ 'L_FtoeC01IK_CtrlZero', 'L_FtoeC02IK_CtrlZero', 'L_FtoeC03IK_CtrlZero', 'L_FtoeC04IK_CtrlZero' ]
toeToeZeros += [ 'L_FtoeD01IK_CtrlZero', 'L_FtoeD02IK_CtrlZero', 'L_FtoeD03IK_CtrlZero', 'L_FtoeD04IK_CtrlZero' ]
toeToeZeros += [ 'L_FtoeE02IK_CtrlZero', 'L_FtoeE03IK_CtrlZero', 'L_FtoeE04IK_CtrlZero' ]

for toeToeZero in toeToeZeros:
    print( toeToeZero )
    cmds.parentConstraint( 'L_Ftoe_Jx', toeToeZero, mo=True )

# R
R_FtoeRigRet = denTR.den_makeToeRig(side='R_', name='Ftoe', toeList=['A','B','C','D','E'], radius=2, doIK=True )
print( R_FtoeRigRet )
R_FtoeRigGrp = R_FtoeRigRet[0]; print( R_FtoeRigGrp )
R_FtoeSpaceINs = R_FtoeRigRet[1]; print( R_FtoeSpaceINs )
R_FtoeSpaceOUTs = R_FtoeRigRet[2]; print( R_FtoeSpaceOUTs )
R_FtoeBindJnts = R_FtoeRigRet[3]; print( R_FtoeBindJnts )
R_FtoeCtrlsALL = R_FtoeRigRet[4]; print( R_FtoeCtrlsALL )
R_FtoeGutsALL = R_FtoeRigRet[5]; print( R_FtoeGutsALL )

denUt.den_connectProxyGeo( Jnts=R_FtoeBindJnts )


R_FtoesSpaceIN = R_FtoeSpaceINs[0]

R_FtoeRigGrp = cmds.parent( R_FtoeRigGrp, RootRigGrp )

cmds.parentConstraint( R_AnkleSpaceOUT, R_FtoesSpaceIN )
cmds.scaleConstraint( R_AnkleSpaceOUT, R_FtoesSpaceIN )

# set ik for fingers
ballToeZeros = [ 'R_FtoeA01IK_CtrlZero', 'R_FtoeE01IK_CtrlZero', ]
for ballToeZero in ballToeZeros:
    print( ballToeZero )
    cmds.parentConstraint( 'R_Fball_Jnt', ballToeZero, mo=True )

toeToeZeros = [ 'R_FtoeA02IK_CtrlZero', 'R_FtoeA03IK_CtrlZero' ]
toeToeZeros += [ 'R_FtoeB01IK_CtrlZero', 'R_FtoeB02IK_CtrlZero', 'R_FtoeB03IK_CtrlZero', 'R_FtoeB04IK_CtrlZero' ]
toeToeZeros += [ 'R_FtoeC01IK_CtrlZero', 'R_FtoeC02IK_CtrlZero', 'R_FtoeC03IK_CtrlZero', 'R_FtoeC04IK_CtrlZero' ]
toeToeZeros += [ 'R_FtoeD01IK_CtrlZero', 'R_FtoeD02IK_CtrlZero', 'R_FtoeD03IK_CtrlZero', 'R_FtoeD04IK_CtrlZero' ]
toeToeZeros += [ 'R_FtoeE02IK_CtrlZero', 'R_FtoeE03IK_CtrlZero', 'R_FtoeE04IK_CtrlZero' ]

for toeToeZero in toeToeZeros:
    print( toeToeZero )
    cmds.parentConstraint( 'R_Ftoe_Jx', toeToeZero, mo=True )

# clean ups
denUt.den_AddSafetyCovers( rigGroup=L_FtoeRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', L_FtoeRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', L_FtoeRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', L_FtoeRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Left_Color', L_FtoeRigGrp[0]+'.Ctrl_Color' )


denUt.den_AddSafetyCovers( rigGroup=R_FtoeRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', R_FtoeRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', R_FtoeRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', R_FtoeRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Right_Color', R_FtoeRigGrp[0]+'.Ctrl_Color' )





######## ============================= ADD ONS =========================================
############################
######## ============================= FIN ADD ON =========================================
####### -------------------------------
# Ears
# ---------------------------------------------------------------------------------------
# use Sluggy fin pivots creation command for ears

EarPivsRet = denAR.den_makeFKappendagePivs( side='L_', name='Ear', jointCount=3, radius=2 )
cmds.parent( EarPivsRet, RootPivGrp ) # put torso pivits under main pivot group

EarPivsRet = denAR.den_makeFKappendagePivs( side='R_', name='Ear', jointCount=3, radius=2 )
cmds.parent( EarPivsRet, RootPivGrp ) # put torso pivits under main pivot group

# reposition pivots

cmds.xform( 'L_EarEnd_Piv', t=( 34.90031814575195, 214.7183074951172, 205.78842163085938 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_Ear_upPiv', t=( 26.658288719093292, 207.99274567306395, 223.06634733413185 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_Ear01_Piv', t=( 10.696591172044066, 207.82224409819372, 214.1207873622626 ), ro=( 103.34482244053224, 30.04818406083061, 13.947320625282932 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_Ear02_Piv', t=( 17.688845979527997, 209.55878206147088, 209.95308986693757 ), ro=( 101.49734629556298, 13.381687551092357, 9.3308112808603 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_Ear03_Piv', t=( 27.083168737038456, 211.10234921423893, 207.68825239762373 ), ro=( 100.22821336897195, 12.439019071335343, 24.82372131420458 ), s=( 1.0, 1.0, 1.0 ) )


cmds.xform( 'R_EarEnd_Piv', t=( 34.90031814575195, 214.7183074951172, 205.78842163085938 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_Ear_upPiv', t=( 26.658288719093292, 207.99274567306395, 223.06634733413185 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_Ear01_Piv', t=( 10.696591172044066, 207.82224409819372, 214.1207873622626 ), ro=( 103.34482244053224, 30.04818406083061, 13.947320625282932 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_Ear02_Piv', t=( 17.688845979527997, 209.55878206147088, 209.95308986693757 ), ro=( 101.49734629556298, 13.381687551092357, 9.3308112808603 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_Ear03_Piv', t=( 27.083168737038456, 211.10234921423893, 207.68825239762373 ), ro=( 100.22821336897195, 12.439019071335343, 24.82372131420458 ), s=( 1.0, 1.0, 1.0 ) )



# ---------------------------------------------------------------------------------------
# use Sluggy fin rig creation command ( FK only ) to make ear rig
# L
L_EarRigRet = denAR.den_makeFKappendageRig( side='L_', name='Ear', jointCount=3, radius=2, ctrlRadius=6.0, secondaryAxisOrient='zup' )
print( L_EarRigRet )
L_EarRigGrp = L_EarRigRet[0]; print( L_EarRigGrp )
L_EarSpaceIN = L_EarRigRet[1][0]; print( L_EarSpaceIN )
L_EarBindJnts = L_EarRigRet[3]; print( L_EarBindJnts )
L_EarCtrls = L_EarRigRet[4]; print( L_EarCtrls )

denUt.den_connectProxyGeo( Jnts=L_EarBindJnts )

L_EarRigGrp = cmds.parent( L_EarRigGrp, RootRigGrp )

L_EarSpaceConstraint = cmds.parentConstraint( HeadSpaceOUT, L_EarSpaceIN, mo=True  )
L_EarSpaceScaleConstraint = cmds.scaleConstraint( HeadSpaceOUT, L_EarSpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=L_EarRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', L_EarRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', L_EarRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', L_EarRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Left_Color', L_EarRigGrp[0]+'.Ctrl_Color' )

# R
R_EarRigRet = denAR.den_makeFKappendageRig( side='R_', name='Ear', jointCount=3, radius=2, ctrlRadius=6.0, secondaryAxisOrient='zup' )
print( R_EarRigRet )
R_EarRigGrp = R_EarRigRet[0]; print( R_EarRigGrp )
R_EarSpaceIN = R_EarRigRet[1][0]; print( R_EarSpaceIN )
R_EarBindJnts = R_EarRigRet[3]; print( R_EarBindJnts )
R_EarCtrls = R_EarRigRet[4]; print( R_EarCtrls )

denUt.den_connectProxyGeo( Jnts=R_EarBindJnts )

R_EarRigGrp = cmds.parent( R_EarRigGrp, RootRigGrp )

R_EarSpaceConstraint = cmds.parentConstraint( HeadSpaceOUT, R_EarSpaceIN, mo=True  )
R_EarSpaceScaleConstraint = cmds.scaleConstraint( HeadSpaceOUT, R_EarSpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=R_EarRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', R_EarRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', R_EarRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', R_EarRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Right_Color', R_EarRigGrp[0]+'.Ctrl_Color' )



#########################################################################################
####### -------------------------------
# Horn
# ---------------------------------------------------------------------------------------
# use Sluggy fin pivots creation command for horn

HornPivsRet = denAR.den_makeFKappendagePivs( side='', name='Horn', jointCount=1, radius=2 )
cmds.parent( HornPivsRet, RootPivGrp ) # put torso pivits under main pivot group


# reposition pivots
cmds.xform( 'Horn_upPiv', t=( 78.23672549310467, 228.33604984078102, 192.44823182598822 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'Horn01_Piv', t=( 4.4, 211.29718121701404, 214.4159409302883 ), ro=( -173.53672753761234, 34.69146685590826, 89.99999990380199 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'HornEnd_Piv', t=( 4.400000095367432, 268.0982666015625, 175.09751892089844 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )

 
# ---------------------------------------------------------------------------------------
# use Sluggy fin rig creation command ( FK only ) to make chinfin rig

HornRigRet = denAR.den_makeFKappendageRig( side='', name='Horn', jointCount=1, radius=2, ctrlRadius=6.0, secondaryAxisOrient='zup' )
print( HornRigRet )
HornRigGrp = HornRigRet[0]; print( HornRigGrp )
HornSpaceIN = HornRigRet[1][0]; print( HornSpaceIN )
HornBindJnts = HornRigRet[3]; print( HornBindJnts )
HornCtrls = HornRigRet[4]; print( HornCtrls )

denUt.den_connectProxyGeo( Jnts=HornBindJnts )

HornRigGrp = cmds.parent( HornRigGrp, RootRigGrp )

HornSpaceConstraint = cmds.parentConstraint( HeadSpaceOUT, HornSpaceIN, mo=True  )
HornSpaceScaleConstraint = cmds.scaleConstraint( HeadSpaceOUT, HornSpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=HornRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', HornRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', HornRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', HornRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Center_Color', HornRigGrp[0]+'.Ctrl_Color' )


#########################################################################################
######## ============================= Make Crest Spikes =========================================
####### -------------------------------
# crest A
# ---------------------------------------------------------------------------------------
# use Sluggy fin pivots creation command for horn

CrestAPivsRet = denAR.den_makeFKappendagePivs( side='', name='CrestA', jointCount=1, radius=2 )
cmds.parent( CrestAPivsRet, RootPivGrp ) # put torso pivits under main pivot group


# reposition pivots
cmds.xform( 'CrestA_upPiv', t=( 89.82726167059792, 206.22112653994822, 218.21163521148816 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'CrestA01_Piv', t=( 0.0, 212.2363089643746, 219.02128323932754 ), ro=( 179.72760986609117, -11.700706598440053, 90.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'CrestAEnd_Piv', t=( 0.0, 238.36009543722264, 224.43159532897656 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )


# ---------------------------------------------------------------------------------------
# use Sluggy fin rig creation command ( FK only ) to make chinfin rig

CrestARigRet = denAR.den_makeFKappendageRig( side='', name='CrestA', jointCount=1, radius=2, ctrlRadius=18, secondaryAxisOrient='zup' )
print( CrestARigRet )
CrestARigGrp = CrestARigRet[0]; print( CrestARigGrp )
CrestASpaceIN = CrestARigRet[1][0]; print( CrestASpaceIN )
CrestABindJnts = CrestARigRet[3]; print( CrestABindJnts )
CrestACtrls = CrestARigRet[4]; print( CrestACtrls )

denUt.den_connectProxyGeo( Jnts=CrestABindJnts )

CrestARigGrp = cmds.parent( CrestARigGrp, RootRigGrp )

CrestASpaceConstraint = cmds.parentConstraint( HeadSpaceOUT, CrestASpaceIN, mo=True  )
CrestASpaceScaleConstraint = cmds.scaleConstraint( HeadSpaceOUT, CrestASpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=CrestARigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', CrestARigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', CrestARigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', CrestARigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Center_Color', CrestARigGrp[0]+'.Ctrl_Color' )




####### -------------------------------
# crest B
# ---------------------------------------------------------------------------------------
# use Sluggy fin pivots creation command for horn

CrestBPivsRet = denAR.den_makeFKappendagePivs( side='', name='CrestB', jointCount=1, radius=2 )
cmds.parent( CrestBPivsRet, RootPivGrp ) # put torso pivits under main pivot group


# reposition pivots
cmds.xform( 'CrestB_upPiv', t=( 89.82726167059792, 210.59974493533826, 194.19985691418793 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'CrestB01_Piv', t=( 0.0, 216.61492735976464, 195.00950494202732 ), ro=( -179.89625457701592, -6.13036707481712, 90.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'CrestBEnd_Piv', t=( 0.0, 251.13203655337531, 198.7168240158694 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )


# ---------------------------------------------------------------------------------------
# use Sluggy fin rig creation command ( FK only ) to make chinfin rig

CrestBRigRet = denAR.den_makeFKappendageRig( side='', name='CrestB', jointCount=1, radius=2, ctrlRadius=18, secondaryAxisOrient='zup' )
print( CrestBRigRet )
CrestBRigGrp = CrestBRigRet[0]; print( CrestBRigGrp )
CrestBSpaceIN = CrestBRigRet[1][0]; print( CrestBSpaceIN )
CrestBBindJnts = CrestBRigRet[3]; print( CrestBBindJnts )
CrestBCtrls = CrestBRigRet[4]; print( CrestBCtrls )

denUt.den_connectProxyGeo( Jnts=CrestBBindJnts )

CrestBRigGrp = cmds.parent( CrestBRigGrp, RootRigGrp )

Neck06Space_OUT = TorsoSpaceOUTs[10]; print( Neck06Space_OUT )


CrestBSpaceConstraint = cmds.parentConstraint( Neck06Space_OUT, CrestBSpaceIN, mo=True  )
CrestBSpaceScaleConstraint = cmds.scaleConstraint( Neck06Space_OUT, CrestBSpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=CrestBRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', CrestBRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', CrestBRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', CrestBRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Center_Color', CrestBRigGrp[0]+'.Ctrl_Color' )


####### -------------------------------
# crest C
# ---------------------------------------------------------------------------------------
# use Sluggy fin pivots creation command for horn

CrestCPivsRet = denAR.den_makeFKappendagePivs( side='', name='CrestC', jointCount=1, radius=2 )
cmds.parent( CrestCPivsRet, RootPivGrp ) # put torso pivits under main pivot group


# reposition pivots
cmds.xform( 'CrestC_upPiv', t=( 89.82726167059792, 206.21545081056044, 167.73418185545003 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'CrestC01_Piv', t=( 0.0, 213.4815347435189, 166.4172973187849 ), ro=( -178.44009285584085, 29.618084573492133, 90.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'CrestCEnd_Piv', t=( 0.0, 245.246660618359, 148.3589301441691 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )


# ---------------------------------------------------------------------------------------
# use Sluggy fin rig creation command ( FK only ) to make chinfin rig

CrestCRigRet = denAR.den_makeFKappendageRig( side='', name='CrestC', jointCount=1, radius=2, ctrlRadius=18, secondaryAxisOrient='zup' )
print( CrestCRigRet )
CrestCRigGrp = CrestCRigRet[0]; print( CrestCRigGrp )
CrestCSpaceIN = CrestCRigRet[1][0]; print( CrestCSpaceIN )
CrestCBindJnts = CrestCRigRet[3]; print( CrestCBindJnts )
CrestCCtrls = CrestCRigRet[4]; print( CrestCCtrls )

denUt.den_connectProxyGeo( Jnts=CrestCBindJnts )

CrestCRigGrp = cmds.parent( CrestCRigGrp, RootRigGrp )

Neck05Space_OUT = TorsoSpaceOUTs[9]; print( Neck05Space_OUT )

CrestCSpaceConstraint = cmds.parentConstraint( Neck05Space_OUT, CrestCSpaceIN, mo=True  )
CrestCSpaceScaleConstraint = cmds.scaleConstraint( Neck05Space_OUT, CrestCSpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=CrestCRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', CrestCRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', CrestCRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', CrestCRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Center_Color', CrestCRigGrp[0]+'.Ctrl_Color' )


####### -------------------------------
# crest D
# ---------------------------------------------------------------------------------------
# use Sluggy fin pivots creation command for horn

CrestDPivsRet = denAR.den_makeFKappendagePivs( side='', name='CrestD', jointCount=1, radius=2 )
cmds.parent( CrestDPivsRet, RootPivGrp ) # put torso pivits under main pivot group


# reposition pivots
cmds.xform( 'CrestD_upPiv', t=( 89.82726167059792, 194.43080806603305, 141.86631780566523 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'CrestD01_Piv', t=( 0.0, 199.85205316807148, 138.04572342703716 ), ro=( -179.63368150607803, 40.14177381626509, 89.99999999999999 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'CrestDEnd_Piv', t=( 0.0, 221.7341138772685, 119.59203364579565 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )


# ---------------------------------------------------------------------------------------
# use Sluggy fin rig creation command ( FK only ) to make chinfin rig

CrestDRigRet = denAR.den_makeFKappendageRig( side='', name='CrestD', jointCount=1, radius=2, ctrlRadius=18, secondaryAxisOrient='zup' )
print( CrestDRigRet )
CrestDRigGrp = CrestDRigRet[0]; print( CrestDRigGrp )
CrestDSpaceIN = CrestDRigRet[1][0]; print( CrestDSpaceIN )
CrestDBindJnts = CrestDRigRet[3]; print( CrestDBindJnts )
CrestDCtrls = CrestDRigRet[4]; print( CrestDCtrls )

denUt.den_connectProxyGeo( Jnts=CrestDBindJnts )

CrestDRigGrp = cmds.parent( CrestDRigGrp, RootRigGrp )

Neck04Space_OUT = TorsoSpaceOUTs[8]; print( Neck04Space_OUT )

CrestDSpaceConstraint = cmds.parentConstraint( Neck04Space_OUT, CrestDSpaceIN, mo=True  )
CrestDSpaceScaleConstraint = cmds.scaleConstraint( Neck04Space_OUT, CrestDSpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=CrestDRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', CrestDRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', CrestDRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', CrestDRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Center_Color', CrestDRigGrp[0]+'.Ctrl_Color' )


####### -------------------------------
# crest E
# ---------------------------------------------------------------------------------------
# use Sluggy fin pivots creation command for horn

CrestEPivsRet = denAR.den_makeFKappendagePivs( side='', name='CrestE', jointCount=1, radius=2 )
cmds.parent( CrestEPivsRet, RootPivGrp ) # put torso pivits under main pivot group


# reposition pivots
cmds.xform( 'CrestE_upPiv', t=( 89.82726167059792, 184.9244187930526, 127.32713421169497 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'CrestE01_Piv', t=( 0.0, 190.34566389509104, 123.50653983306697 ), ro=( -177.863329590779, 65.52640176744157, 90.00000000000006 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'CrestEEnd_Piv', t=( 0.0, 197.40894132581855, 107.98864673906954 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )


# ---------------------------------------------------------------------------------------
# use Sluggy fin rig creation command ( FK only ) to make chinfin rig

CrestERigRet = denAR.den_makeFKappendageRig( side='', name='CrestE', jointCount=1, radius=2, ctrlRadius=18, secondaryAxisOrient='zup' )
print( CrestERigRet )
CrestERigGrp = CrestERigRet[0]; print( CrestERigGrp )
CrestESpaceIN = CrestERigRet[1][0]; print( CrestESpaceIN )
CrestEBindJnts = CrestERigRet[3]; print( CrestEBindJnts )
CrestECtrls = CrestERigRet[4]; print( CrestECtrls )

denUt.den_connectProxyGeo( Jnts=CrestEBindJnts )

CrestERigGrp = cmds.parent( CrestERigGrp, RootRigGrp )

Neck03Space_OUT = TorsoSpaceOUTs[7]; print( Neck03Space_OUT )

CrestESpaceConstraint = cmds.parentConstraint( Neck03Space_OUT, CrestESpaceIN, mo=True  )
CrestESpaceScaleConstraint = cmds.scaleConstraint( Neck03Space_OUT, CrestESpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=CrestERigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', CrestERigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', CrestERigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', CrestERigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Center_Color', CrestERigGrp[0]+'.Ctrl_Color' )


####### =============================================================================================================================
####### -------------------------------
# Make Chinfin
# ---------------------------------------------------------------------------------------
# use Sluggy fin pivots creation command for chinfin

ChinfinPivsRet = denAR.den_makeFKappendagePivs( side='', name='Chinfin', jointCount=2, radius=2 )
cmds.parent( ChinfinPivsRet, RootPivGrp ) # put torso pivits under main pivot group


# reposition pivots
cmds.xform( 'Chinfin01_Piv', t=( 0.0, 176.29407850447365, 221.71648110825052 ), ro=( -90.0, 41.98719169934646, -90.00000000000003 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'Chinfin02_Piv', t=( 0.0, 173.66575579459075, 219.35099239608465 ), ro=( 90.0, 59.817130691046515, -90.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'ChinfinEnd_Piv', t=( 0.0, 170.648051942503, 214.16249040293354 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'Chinfin_upPiv', t=( 32.245715552903015, 175.42310364825838, 208.6722128443873 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )


# ---------------------------------------------------------------------------------------
# use Sluggy fin rig creation command ( FK only ) to make chinfin rig

ChinfinRigRet = denAR.den_makeFKappendageRig( side='', name='Chinfin', jointCount=2, radius=2, ctrlRadius=6.0, secondaryAxisOrient='zup' )
print( ChinfinRigRet )
ChinfinRigGrp = ChinfinRigRet[0]; print( ChinfinRigGrp )
ChinfinSpaceIN = ChinfinRigRet[1][0]; print( ChinfinSpaceIN )
ChinfinBindJnts = ChinfinRigRet[3]; print( ChinfinBindJnts )
ChinfinCtrls = ChinfinRigRet[4]; print( ChinfinCtrls )

denUt.den_connectProxyGeo( Jnts=ChinfinBindJnts )

ChinfinRigGrp = cmds.parent( ChinfinRigGrp, RootRigGrp )

ChinfinSpaceConstraint = cmds.parentConstraint( JawSpaceOUT, ChinfinSpaceIN, mo=True  )
ChinfinSpaceScaleConstraint = cmds.scaleConstraint( JawSpaceOUT, ChinfinSpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=ChinfinRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', ChinfinRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', ChinfinRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', ChinfinRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Center_Color', ChinfinRigGrp[0]+'.Ctrl_Color' )



####### =============================================================================================================================
####### -------------------------------
# Make Headfins
# ---------------------------------------------------------------------------------------
# use Sluggy fin pivots creation command for ears

HeadfinPivsRet = denAR.den_makeFKappendagePivs( side='L_', name='Headfin', jointCount=3, radius=2 )
cmds.parent( HeadfinPivsRet, RootPivGrp ) # put torso pivits under main pivot group

HeadfinPivsRet = denAR.den_makeFKappendagePivs( side='R_', name='Headfin', jointCount=3, radius=2 )
cmds.parent( HeadfinPivsRet, RootPivGrp ) # put torso pivits under main pivot group

# reposition pivots
cmds.xform( 'L_HeadfinEnd_Piv', t=( 31.082395553588867, 179.7672882080078, 187.78573608398438 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_Headfin01_Piv', t=( 12.922269535574031, 199.87607418120643, 209.4708202899137 ), ro=( 64.70124360999465, 42.60573558566102, -44.914737428023855 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_Headfin03_Piv', t=( 21.46491035279459, 191.2497711181656, 198.5139077494346 ), ro=( 62.50643647856504, 35.61240636937876, -50.05116975221161 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_Headfin_upPiv', t=( 31.419893838645823, 191.525884242208, 212.54401821108945 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_Headfin02_Piv', t=( 17.49462740839529, 195.31730446452215, 203.53239705872844 ), ro=( 63.98090082925004, 41.441717821096816, -45.69319396171107 ), s=( 1.0, 1.0, 1.0 ) )


cmds.xform( 'R_HeadfinEnd_Piv', t=( 31.082395553588867, 179.7672882080078, 187.78573608398438 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_Headfin01_Piv', t=( 12.922269535574031, 199.87607418120643, 209.4708202899137 ), ro=( 64.70124360999465, 42.60573558566102, -44.914737428023855 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_Headfin03_Piv', t=( 21.46491035279459, 191.2497711181656, 198.5139077494346 ), ro=( 62.50643647856504, 35.61240636937876, -50.05116975221161 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_Headfin_upPiv', t=( 31.419893838645823, 191.525884242208, 212.54401821108945 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_Headfin02_Piv', t=( 17.49462740839529, 195.31730446452215, 203.53239705872844 ), ro=( 63.98090082925004, 41.441717821096816, -45.69319396171107 ), s=( 1.0, 1.0, 1.0 ) )


# ---------------------------------------------------------------------------------------
# use Sluggy fin rig creation command ( FK only ) to make ear rig
# L
L_HeadfinRigRet = denAR.den_makeFKappendageRig( side='L_', name='Headfin', jointCount=3, radius=2, ctrlRadius=6.0, secondaryAxisOrient='zup' )
print( L_HeadfinRigRet )
L_HeadfinRigGrp = L_HeadfinRigRet[0]; print( L_HeadfinRigGrp )
L_HeadfinSpaceIN = L_HeadfinRigRet[1][0]; print( L_HeadfinSpaceIN )
L_HeadfinBindJnts = L_HeadfinRigRet[3]; print( L_HeadfinBindJnts )
L_HeadfinCtrls = L_HeadfinRigRet[4]; print( L_HeadfinCtrls )

denUt.den_connectProxyGeo( Jnts=L_HeadfinBindJnts )

L_HeadfinRigGrp = cmds.parent( L_HeadfinRigGrp, RootRigGrp )

L_HeadfinSpaceConstraint = cmds.parentConstraint( HeadSpaceOUT, L_HeadfinSpaceIN, mo=True  )
L_HeadfinSpaceScaleConstraint = cmds.scaleConstraint( HeadSpaceOUT, L_HeadfinSpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=L_HeadfinRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', L_HeadfinRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', L_HeadfinRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', L_HeadfinRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Left_Color', L_HeadfinRigGrp[0]+'.Ctrl_Color' )

# R
R_HeadfinRigRet = denAR.den_makeFKappendageRig( side='R_', name='Headfin', jointCount=3, radius=2, ctrlRadius=6.0, secondaryAxisOrient='zup' )
print( R_HeadfinRigRet )
R_HeadfinRigGrp = R_HeadfinRigRet[0]; print( R_HeadfinRigGrp )
R_HeadfinSpaceIN = R_HeadfinRigRet[1][0]; print( R_HeadfinSpaceIN )
R_HeadfinBindJnts = R_HeadfinRigRet[3]; print( R_HeadfinBindJnts )
R_HeadfinCtrls = R_HeadfinRigRet[4]; print( R_HeadfinCtrls )

denUt.den_connectProxyGeo( Jnts=R_HeadfinBindJnts )

R_HeadfinRigGrp = cmds.parent( R_HeadfinRigGrp, RootRigGrp )

R_HeadfinSpaceConstraint = cmds.parentConstraint( HeadSpaceOUT, R_HeadfinSpaceIN, mo=True  )
R_HeadfinSpaceScaleConstraint = cmds.scaleConstraint( HeadSpaceOUT, R_HeadfinSpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=R_HeadfinRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', R_HeadfinRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', R_HeadfinRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', R_HeadfinRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Right_Color', R_HeadfinRigGrp[0]+'.Ctrl_Color' )


#################################################=====================================================================================

##################       Make Spike Rigs for Left + Right Sides, using same 2 joint 1 control structure           ##################

#################################################=====================================================================================
######## ============================= Make Shoulder Spikes =========================================
####### -------------------------------
# spike sld A
# ---------------------------------------------------------------------------------------
# use Sluggy fin pivots creation command

FinAPivsRet = denAR.den_makeFKappendagePivs( side='L_', name='FinA', jointCount=1, radius=2 )
cmds.parent( FinAPivsRet, RootPivGrp ) # put torso pivits under main pivot group

FinAPivsRet = denAR.den_makeFKappendagePivs( side='R_', name='FinA', jointCount=1, radius=2 )
cmds.parent( FinAPivsRet, RootPivGrp ) # put torso pivits under main pivot group

# reposition pivots
cmds.xform( 'L_FinA_upPiv', t=( 102.55470322180483, 119.97928392590832, 69.57244337210213 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinA01_Piv', t=( 25.8713413297698, 118.87928392590834, 69.57244337210213 ), ro=( -167.8802443731546, -75.05942547025516, 78.29119721026633 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinAEnd_Piv', t=( 33.47648453401122, 124.18687637155124, 89.88583358383383 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )


cmds.xform( 'R_FinA_upPiv', t=( 102.55470322180483, 119.97928392590832, 69.57244337210213 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinA01_Piv', t=( 25.8713413297698, 118.87928392590834, 69.57244337210213 ), ro=( -167.8802443731546, -75.05942547025516, 78.29119721026633 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinAEnd_Piv', t=( 33.47648453401122, 124.18687637155124, 89.88583358383383 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )


# ---------------------------------------------------------------------------------------
# use Sluggy fin rig creation command ( FK only ) to make ear rig
# L
L_FinARigRet = denAR.den_makeFKappendageRig( side='L_', name='FinA', jointCount=1, radius=2, ctrlRadius=30.0, secondaryAxisOrient='zup' )
print( L_FinARigRet )
L_FinARigGrp = L_FinARigRet[0]; print( L_FinARigGrp )
L_FinASpaceIN = L_FinARigRet[1][0]; print( L_FinASpaceIN )
L_FinABindJnts = L_FinARigRet[3]; print( L_FinABindJnts )
L_FinACtrls = L_FinARigRet[4]; print( L_FinACtrls )

denUt.den_connectProxyGeo( Jnts=L_FinABindJnts )

L_FinARigGrp = cmds.parent( L_FinARigGrp, RootRigGrp )



L_FinASpaceConstraint = cmds.parentConstraint( 'L_ShldRest_Jx', L_FinASpaceIN, mo=True  )
L_FinASpaceScaleConstraint = cmds.scaleConstraint( 'L_ShldRest_Jx', L_FinASpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=L_FinARigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', L_FinARigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', L_FinARigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', L_FinARigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Left_Color', L_FinARigGrp[0]+'.Ctrl_Color' )

# R
R_FinARigRet = denAR.den_makeFKappendageRig( side='R_', name='FinA', jointCount=1, radius=2, ctrlRadius=30.0, secondaryAxisOrient='zup' )
print( R_FinARigRet )
R_FinARigGrp = R_FinARigRet[0]; print( R_FinARigGrp )
R_FinASpaceIN = R_FinARigRet[1][0]; print( R_FinASpaceIN )
R_FinABindJnts = R_FinARigRet[3]; print( R_FinABindJnts )
R_FinACtrls = R_FinARigRet[4]; print( R_FinACtrls )

denUt.den_connectProxyGeo( Jnts=R_FinABindJnts )

R_FinARigGrp = cmds.parent( R_FinARigGrp, RootRigGrp )

R_FinASpaceConstraint = cmds.parentConstraint( 'R_ShldRest_Jx', R_FinASpaceIN, mo=True  )
R_FinASpaceScaleConstraint = cmds.scaleConstraint( 'R_ShldRest_Jx', R_FinASpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=R_FinARigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', R_FinARigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', R_FinARigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', R_FinARigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Right_Color', R_FinARigGrp[0]+'.Ctrl_Color' )



####### -------------------------------
# spike sld B
# ---------------------------------------------------------------------------------------
# use Sluggy fin pivots creation command

FinBPivsRet = denAR.den_makeFKappendagePivs( side='L_', name='FinB', jointCount=1, radius=2 )
cmds.parent( FinBPivsRet, RootPivGrp ) # put torso pivits under main pivot group

FinBPivsRet = denAR.den_makeFKappendagePivs( side='R_', name='FinB', jointCount=1, radius=2 )
cmds.parent( FinBPivsRet, RootPivGrp ) # put torso pivits under main pivot group

# reposition pivots
cmds.xform( 'L_FinB01_Piv', t=( 25.8713413297698, 143.7148699907943, 62.328730769843716 ), ro=( -176.78695635923987, -9.098817731076396, 71.27756169199766 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinB_upPiv', t=( 102.55470322180483, 177.97782244106244, 62.328730769843716 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinBEnd_Piv', t=( 25.871, 201.62561347664717, 72.12149077353344 ) )


cmds.xform( 'R_FinB01_Piv', t=( 25.8713413297698, 143.7148699907943, 62.328730769843716 ), ro=( -176.78695635923987, -9.098817731076396, 71.27756169199766 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinB_upPiv', t=( 102.55470322180483, 177.97782244106244, 62.328730769843716 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinBEnd_Piv', t=( 25.871, 201.62561347664717, 72.12149077353344 ) )


# ---------------------------------------------------------------------------------------
# use Sluggy fin rig creation command ( FK only ) to make ear rig
# L
L_FinBRigRet = denAR.den_makeFKappendageRig( side='L_', name='FinB', jointCount=1, radius=2, ctrlRadius=30.0, secondaryAxisOrient='zup' )
print( L_FinBRigRet )
L_FinBRigGrp = L_FinBRigRet[0]; print( L_FinBRigGrp )
L_FinBSpaceIN = L_FinBRigRet[1][0]; print( L_FinBSpaceIN )
L_FinBBindJnts = L_FinBRigRet[3]; print( L_FinBBindJnts )
L_FinBCtrls = L_FinBRigRet[4]; print( L_FinBCtrls )

denUt.den_connectProxyGeo( Jnts=L_FinBBindJnts )

L_FinBRigGrp = cmds.parent( L_FinBRigGrp, RootRigGrp )


L_FinBSpaceConstraint = cmds.parentConstraint( 'L_ShldRest_Jx', L_FinBSpaceIN, mo=True  )
L_FinBSpaceScaleConstraint = cmds.scaleConstraint( 'L_ShldRest_Jx', L_FinBSpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=L_FinBRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', L_FinBRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', L_FinBRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', L_FinBRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Left_Color', L_FinBRigGrp[0]+'.Ctrl_Color' )

# R
R_FinBRigRet = denAR.den_makeFKappendageRig( side='R_', name='FinB', jointCount=1, radius=2, ctrlRadius=30.0, secondaryAxisOrient='zup' )
print( R_FinBRigRet )
R_FinBRigGrp = R_FinBRigRet[0]; print( R_FinBRigGrp )
R_FinBSpaceIN = R_FinBRigRet[1][0]; print( R_FinBSpaceIN )
R_FinBBindJnts = R_FinBRigRet[3]; print( R_FinBBindJnts )
R_FinBCtrls = R_FinBRigRet[4]; print( R_FinBCtrls )

denUt.den_connectProxyGeo( Jnts=R_FinBBindJnts )

R_FinBRigGrp = cmds.parent( R_FinBRigGrp, RootRigGrp )

R_FinBSpaceConstraint = cmds.parentConstraint( 'R_ShldRest_Jx', R_FinBSpaceIN, mo=True  )
R_FinBSpaceScaleConstraint = cmds.scaleConstraint( 'R_ShldRest_Jx', R_FinBSpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=R_FinBRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', R_FinBRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', R_FinBRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', R_FinBRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Right_Color', R_FinBRigGrp[0]+'.Ctrl_Color' )



####### -------------------------------
# spike sld C
# ---------------------------------------------------------------------------------------
# use Sluggy fin pivots creation command

FinCPivsRet = denAR.den_makeFKappendagePivs( side='L_', name='FinC', jointCount=1, radius=2 )
cmds.parent( FinCPivsRet, RootPivGrp ) # put torso pivits under main pivot group

FinCPivsRet = denAR.den_makeFKappendagePivs( side='R_', name='FinC', jointCount=1, radius=2 )
cmds.parent( FinCPivsRet, RootPivGrp ) # put torso pivits under main pivot group

# reposition pivots
cmds.xform( 'L_FinC_upPiv', t=( 102.55470322180483, 182.1698301449211, 29.79076621132196 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinC01_Piv', t=( 25.8713413297698, 154.69393778661455, 41.76793107948948 ), ro=( 178.0457965461527, 28.561575758287887, 90.00036541713965 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinCEnd_Piv', t=( 25.871, 208.21305415413931, 12.634905261634763 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )

cmds.xform( 'R_FinC_upPiv', t=( 102.55470322180483, 182.1698301449211, 29.79076621132196 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinC01_Piv', t=( 25.8713413297698, 154.69393778661455, 41.76793107948948 ), ro=( 178.0457965461527, 28.561575758287887, 90.00036541713965 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinCEnd_Piv', t=( 25.871, 208.21305415413931, 12.634905261634763 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )


# ---------------------------------------------------------------------------------------
# use Sluggy fin rig creation command ( FK only ) to make ear rig
# L
L_FinCRigRet = denAR.den_makeFKappendageRig( side='L_', name='FinC', jointCount=1, radius=2, ctrlRadius=30.0, secondaryAxisOrient='zup' )
print( L_FinCRigRet )
L_FinCRigGrp = L_FinCRigRet[0]; print( L_FinCRigGrp )
L_FinCSpaceIN = L_FinCRigRet[1][0]; print( L_FinCSpaceIN )
L_FinCBindJnts = L_FinCRigRet[3]; print( L_FinCBindJnts )
L_FinCCtrls = L_FinCRigRet[4]; print( L_FinCCtrls )

denUt.den_connectProxyGeo( Jnts=L_FinCBindJnts )

L_FinCRigGrp = cmds.parent( L_FinCRigGrp, RootRigGrp )


L_FinCSpaceConstraint = cmds.parentConstraint( 'L_ShldRest_Jx', L_FinCSpaceIN, mo=True  )
L_FinCSpaceScaleConstraint = cmds.scaleConstraint( 'L_ShldRest_Jx', L_FinCSpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=L_FinCRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', L_FinCRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', L_FinCRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', L_FinCRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Left_Color', L_FinCRigGrp[0]+'.Ctrl_Color' )

# R
R_FinCRigRet = denAR.den_makeFKappendageRig( side='R_', name='FinC', jointCount=1, radius=2, ctrlRadius=30.0, secondaryAxisOrient='zup' )
print( R_FinCRigRet )
R_FinCRigGrp = R_FinCRigRet[0]; print( R_FinCRigGrp )
R_FinCSpaceIN = R_FinCRigRet[1][0]; print( R_FinCSpaceIN )
R_FinCBindJnts = R_FinCRigRet[3]; print( R_FinCBindJnts )
R_FinCCtrls = R_FinCRigRet[4]; print( R_FinCCtrls )

denUt.den_connectProxyGeo( Jnts=R_FinCBindJnts )

R_FinCRigGrp = cmds.parent( R_FinCRigGrp, RootRigGrp )

R_FinCSpaceConstraint = cmds.parentConstraint( 'R_ShldRest_Jx', R_FinCSpaceIN, mo=True  )
R_FinCSpaceScaleConstraint = cmds.scaleConstraint( 'R_ShldRest_Jx', R_FinCSpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=R_FinCRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', R_FinCRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', R_FinCRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', R_FinCRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Right_Color', R_FinCRigGrp[0]+'.Ctrl_Color' )




####### -------------------------------
# spike sld D
# ---------------------------------------------------------------------------------------
# use Sluggy fin pivots creation command

FinDPivsRet = denAR.den_makeFKappendagePivs( side='L_', name='FinD', jointCount=1, radius=2 )
cmds.parent( FinDPivsRet, RootPivGrp ) # put torso pivits under main pivot group

FinDPivsRet = denAR.den_makeFKappendagePivs( side='R_', name='FinD', jointCount=1, radius=2 )
cmds.parent( FinDPivsRet, RootPivGrp ) # put torso pivits under main pivot group

# reposition pivots
cmds.xform( 'L_FinD_upPiv', t=( 102.55470322180483, 170.79877146062003, -9.756699145051732 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinD01_Piv', t=( 12.405785111590006, 149.84830425789238, 7.0057775038736665 ), ro=( -178.71817680578272, 34.352892755678965, 90.00060265444209 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinDEnd_Piv', t=( 12.405443781820207, 182.29944876140755, -15.174817598857878 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )

cmds.xform( 'R_FinD_upPiv', t=( 102.55470322180483, 170.79877146062003, -9.756699145051732 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinD01_Piv', t=( 12.405785111590006, 149.84830425789238, 7.0057775038736665 ), ro=( -178.71817680578272, 34.352892755678965, 90.00060265444209 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinDEnd_Piv', t=( 12.405443781820207, 182.29944876140755, -15.174817598857878 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )


# ---------------------------------------------------------------------------------------
# use Sluggy fin rig creation command ( FK only ) to make ear rig
# L
L_FinDRigRet = denAR.den_makeFKappendageRig( side='L_', name='FinD', jointCount=1, radius=2, ctrlRadius=30.0, secondaryAxisOrient='zup' )
print( L_FinDRigRet )
L_FinDRigGrp = L_FinDRigRet[0]; print( L_FinDRigGrp )
L_FinDSpaceIN = L_FinDRigRet[1][0]; print( L_FinDSpaceIN )
L_FinDBindJnts = L_FinDRigRet[3]; print( L_FinDBindJnts )
L_FinDCtrls = L_FinDRigRet[4]; print( L_FinDCtrls )

denUt.den_connectProxyGeo( Jnts=L_FinDBindJnts )

L_FinDRigGrp = cmds.parent( L_FinDRigGrp, RootRigGrp )


L_FinDSpaceConstraint = cmds.parentConstraint( 'Spine03_Jnt', L_FinDSpaceIN, mo=True  )
L_FinDSpaceScaleConstraint = cmds.scaleConstraint( 'Spine03_Jnt', L_FinDSpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=L_FinDRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', L_FinDRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', L_FinDRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', L_FinDRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Left_Color', L_FinDRigGrp[0]+'.Ctrl_Color' )

# R
R_FinDRigRet = denAR.den_makeFKappendageRig( side='R_', name='FinD', jointCount=1, radius=2, ctrlRadius=30.0, secondaryAxisOrient='zup' )
print( R_FinDRigRet )
R_FinDRigGrp = R_FinDRigRet[0]; print( R_FinDRigGrp )
R_FinDSpaceIN = R_FinDRigRet[1][0]; print( R_FinDSpaceIN )
R_FinDBindJnts = R_FinDRigRet[3]; print( R_FinDBindJnts )
R_FinDCtrls = R_FinDRigRet[4]; print( R_FinDCtrls )

denUt.den_connectProxyGeo( Jnts=R_FinDBindJnts )

R_FinDRigGrp = cmds.parent( R_FinDRigGrp, RootRigGrp )

R_FinDSpaceConstraint = cmds.parentConstraint( 'Spine03_Jnt', R_FinDSpaceIN, mo=True  )
R_FinDSpaceScaleConstraint = cmds.scaleConstraint( 'Spine03_Jnt', R_FinDSpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=R_FinDRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', R_FinDRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', R_FinDRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', R_FinDRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Right_Color', R_FinDRigGrp[0]+'.Ctrl_Color' )


####### -------------------------------
# spike sld E
# ---------------------------------------------------------------------------------------
# use Sluggy fin pivots creation command

FinEPivsRet = denAR.den_makeFKappendagePivs( side='L_', name='FinE', jointCount=1, radius=2 )
cmds.parent( FinEPivsRet, RootPivGrp ) # put torso pivits under main pivot group

FinEPivsRet = denAR.den_makeFKappendagePivs( side='R_', name='FinE', jointCount=1, radius=2 )
cmds.parent( FinEPivsRet, RootPivGrp ) # put torso pivits under main pivot group

# reposition pivots
cmds.xform( 'L_FinE_upPiv', t=( 102.55470322180483, 158.466872510283, -25.518960362480367 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinE01_Piv', t=( 11.774981847249727, 150.84318967725062, -18.065335063954485 ), ro=( -179.64960158696638, 41.377827399291256, 90.0015714191527 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinEEnd_Piv', t=( 11.774640517479927, 163.28847214257055, -29.02877091100081 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )

cmds.xform( 'R_FinE_upPiv', t=( 102.55470322180483, 158.466872510283, -25.518960362480367 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinE01_Piv', t=( 11.774981847249727, 150.84318967725062, -18.065335063954485 ), ro=( -179.64960158696638, 41.377827399291256, 90.0015714191527 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinEEnd_Piv', t=( 11.774640517479927, 163.28847214257055, -29.02877091100081 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )


# ---------------------------------------------------------------------------------------
# use Sluggy fin rig creation command ( FK only ) to make ear rig
# L
L_FinERigRet = denAR.den_makeFKappendageRig( side='L_', name='FinE', jointCount=1, radius=2, ctrlRadius=30.0, secondaryAxisOrient='zup' )
print( L_FinERigRet )
L_FinERigGrp = L_FinERigRet[0]; print( L_FinERigGrp )
L_FinESpaceIN = L_FinERigRet[1][0]; print( L_FinESpaceIN )
L_FinEBindJnts = L_FinERigRet[3]; print( L_FinEBindJnts )
L_FinECtrls = L_FinERigRet[4]; print( L_FinECtrls )

denUt.den_connectProxyGeo( Jnts=L_FinEBindJnts )

L_FinERigGrp = cmds.parent( L_FinERigGrp, RootRigGrp )


L_FinESpaceConstraint = cmds.parentConstraint( 'Spine02_Jnt', L_FinESpaceIN, mo=True  )
L_FinESpaceScaleConstraint = cmds.scaleConstraint( 'Spine02_Jnt', L_FinESpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=L_FinERigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', L_FinERigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', L_FinERigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', L_FinERigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Left_Color', L_FinERigGrp[0]+'.Ctrl_Color' )

# R
R_FinERigRet = denAR.den_makeFKappendageRig( side='R_', name='FinE', jointCount=1, radius=2, ctrlRadius=30.0, secondaryAxisOrient='zup' )
print( R_FinERigRet )
R_FinERigGrp = R_FinERigRet[0]; print( R_FinERigGrp )
R_FinESpaceIN = R_FinERigRet[1][0]; print( R_FinESpaceIN )
R_FinEBindJnts = R_FinERigRet[3]; print( R_FinEBindJnts )
R_FinECtrls = R_FinERigRet[4]; print( R_FinECtrls )

denUt.den_connectProxyGeo( Jnts=R_FinEBindJnts )

R_FinERigGrp = cmds.parent( R_FinERigGrp, RootRigGrp )

R_FinESpaceConstraint = cmds.parentConstraint( 'Spine02_Jnt', R_FinESpaceIN, mo=True  )
R_FinESpaceScaleConstraint = cmds.scaleConstraint( 'Spine02_Jnt', R_FinESpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=R_FinERigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', R_FinERigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', R_FinERigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', R_FinERigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Right_Color', R_FinERigGrp[0]+'.Ctrl_Color' )



####### -------------------------------
# spike sld F
# ---------------------------------------------------------------------------------------
# use Sluggy fin pivots creation command

FinFPivsRet = denAR.den_makeFKappendagePivs( side='L_', name='FinF', jointCount=1, radius=2 )
cmds.parent( FinFPivsRet, RootPivGrp ) # put torso pivits under main pivot group

FinFPivsRet = denAR.den_makeFKappendagePivs( side='R_', name='FinF', jointCount=1, radius=2 )
cmds.parent( FinFPivsRet, RootPivGrp ) # put torso pivits under main pivot group

# reposition pivots
cmds.xform( 'L_FinF_upPiv', t=( 98.37742281117772, 154.00926379560894, -89.32765189545755 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinF01_Piv', t=( 7.597701436622621, 145.95419947405972, -83.4557587214934 ), ro=( 179.08510221651892, 44.44687353270299, 89.99901314455089 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinFEnd_Piv', t=( 7.598, 163.28847214257055, -100.45853540777551 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )

cmds.xform( 'R_FinF_upPiv', t=( 98.37742281117772, 154.00926379560894, -89.32765189545755 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinF01_Piv', t=( 7.597701436622621, 145.95419947405972, -83.4557587214934 ), ro=( 179.08510221651892, 44.44687353270299, 89.99901314455089 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinFEnd_Piv', t=( 7.598, 163.28847214257055, -100.45853540777551 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )


# ---------------------------------------------------------------------------------------
# use Sluggy fin rig creation command ( FK only ) to make ear rig
# L
L_FinFRigRet = denAR.den_makeFKappendageRig( side='L_', name='FinF', jointCount=1, radius=2, ctrlRadius=24.0, secondaryAxisOrient='zup' )
print( L_FinFRigRet )
L_FinFRigGrp = L_FinFRigRet[0]; print( L_FinFRigGrp )
L_FinFSpaceIN = L_FinFRigRet[1][0]; print( L_FinFSpaceIN )
L_FinFBindJnts = L_FinFRigRet[3]; print( L_FinFBindJnts )
L_FinFCtrls = L_FinFRigRet[4]; print( L_FinFCtrls )

denUt.den_connectProxyGeo( Jnts=L_FinFBindJnts )

L_FinFRigGrp = cmds.parent( L_FinFRigGrp, RootRigGrp )


L_FinFSpaceConstraint = cmds.parentConstraint( 'L_Hip_Jx', L_FinFSpaceIN, mo=True  )
L_FinFSpaceScaleConstraint = cmds.scaleConstraint( 'L_Hip_Jx', L_FinFSpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=L_FinFRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', L_FinFRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', L_FinFRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', L_FinFRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Left_Color', L_FinFRigGrp[0]+'.Ctrl_Color' )

# R
R_FinFRigRet = denAR.den_makeFKappendageRig( side='R_', name='FinF', jointCount=1, radius=2, ctrlRadius=24.0, secondaryAxisOrient='zup' )
print( R_FinFRigRet )
R_FinFRigGrp = R_FinFRigRet[0]; print( R_FinFRigGrp )
R_FinFSpaceIN = R_FinFRigRet[1][0]; print( R_FinFSpaceIN )
R_FinFBindJnts = R_FinFRigRet[3]; print( R_FinFBindJnts )
R_FinFCtrls = R_FinFRigRet[4]; print( R_FinFCtrls )

denUt.den_connectProxyGeo( Jnts=R_FinFBindJnts )

R_FinFRigGrp = cmds.parent( R_FinFRigGrp, RootRigGrp )

R_FinFSpaceConstraint = cmds.parentConstraint( 'L_Hip_Jx', R_FinFSpaceIN, mo=True  )
R_FinFSpaceScaleConstraint = cmds.scaleConstraint( 'L_Hip_Jx', R_FinFSpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=R_FinFRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', R_FinFRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', R_FinFRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', R_FinFRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Right_Color', R_FinFRigGrp[0]+'.Ctrl_Color' )





####### -------------------------------
# spike sld G
# ---------------------------------------------------------------------------------------
# use Sluggy fin pivots creation command

FinGPivsRet = denAR.den_makeFKappendagePivs( side='L_', name='FinG', jointCount=1, radius=2 )
cmds.parent( FinGPivsRet, RootPivGrp ) # put torso pivits under main pivot group

FinGPivsRet = denAR.den_makeFKappendagePivs( side='R_', name='FinG', jointCount=1, radius=2 )
cmds.parent( FinGPivsRet, RootPivGrp ) # put torso pivits under main pivot group

# reposition pivots
cmds.xform( 'L_FinGEnd_Piv', t=( 7.598, 159.18005904029042, -153.71574228918467 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinG01_Piv', t=( 7.597701436622621, 130.89001809903257, -131.84373525945944 ), ro=( 179.82199404714856, 37.70884722298978, 89.99939532201053 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinG_upPiv', t=( 98.37742281117772, 138.9450824205818, -137.7156284334236 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )

cmds.xform( 'R_FinGEnd_Piv', t=( 7.598, 159.18005904029042, -153.71574228918467 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinG01_Piv', t=( 7.597701436622621, 130.89001809903257, -131.84373525945944 ), ro=( 179.82199404714856, 37.70884722298978, 89.99939532201053 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinG_upPiv', t=( 98.37742281117772, 138.9450824205818, -137.7156284334236 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )


# ---------------------------------------------------------------------------------------
# use Sluggy fin rig creation command ( FK only ) to make ear rig
# L
L_FinGRigRet = denAR.den_makeFKappendageRig( side='L_', name='FinG', jointCount=1, radius=2, ctrlRadius=24.0, secondaryAxisOrient='zup' )
print( L_FinGRigRet )
L_FinGRigGrp = L_FinGRigRet[0]; print( L_FinGRigGrp )
L_FinGSpaceIN = L_FinGRigRet[1][0]; print( L_FinGSpaceIN )
L_FinGBindJnts = L_FinGRigRet[3]; print( L_FinGBindJnts )
L_FinGCtrls = L_FinGRigRet[4]; print( L_FinGCtrls )

denUt.den_connectProxyGeo( Jnts=L_FinGBindJnts )

L_FinGRigGrp = cmds.parent( L_FinGRigGrp, RootRigGrp )


L_FinGSpaceConstraint = cmds.parentConstraint( 'Tail01_Jnt', L_FinGSpaceIN, mo=True  )
L_FinGSpaceScaleConstraint = cmds.scaleConstraint( 'Tail01_Jnt', L_FinGSpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=L_FinGRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', L_FinGRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', L_FinGRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', L_FinGRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Left_Color', L_FinGRigGrp[0]+'.Ctrl_Color' )

# R
R_FinGRigRet = denAR.den_makeFKappendageRig( side='R_', name='FinG', jointCount=1, radius=2, ctrlRadius=24.0, secondaryAxisOrient='zup' )
print( R_FinGRigRet )
R_FinGRigGrp = R_FinGRigRet[0]; print( R_FinGRigGrp )
R_FinGSpaceIN = R_FinGRigRet[1][0]; print( R_FinGSpaceIN )
R_FinGBindJnts = R_FinGRigRet[3]; print( R_FinGBindJnts )
R_FinGCtrls = R_FinGRigRet[4]; print( R_FinGCtrls )

denUt.den_connectProxyGeo( Jnts=R_FinGBindJnts )

R_FinGRigGrp = cmds.parent( R_FinGRigGrp, RootRigGrp )

R_FinGSpaceConstraint = cmds.parentConstraint( 'Tail01_Jnt', R_FinGSpaceIN, mo=True  )
R_FinGSpaceScaleConstraint = cmds.scaleConstraint( 'Tail01_Jnt', R_FinGSpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=R_FinGRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', R_FinGRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', R_FinGRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', R_FinGRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Right_Color', R_FinGRigGrp[0]+'.Ctrl_Color' )







####### -------------------------------
# spike sld H
# ---------------------------------------------------------------------------------------
# use Sluggy fin pivots creation command

FinHPivsRet = denAR.den_makeFKappendagePivs( side='L_', name='FinH', jointCount=1, radius=2 )
cmds.parent( FinHPivsRet, RootPivGrp ) # put torso pivits under main pivot group

FinHPivsRet = denAR.den_makeFKappendagePivs( side='R_', name='FinH', jointCount=1, radius=2 )
cmds.parent( FinHPivsRet, RootPivGrp ) # put torso pivits under main pivot group

# reposition pivots
cmds.xform( 'L_FinH_upPiv', t=( 98.34687893282609, 134.06274677435147, -200.74126084190345 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinH01_Piv', t=( 7.597701436622621, 121.47801002727843, -190.0587481477165 ), ro=( -178.97197134064876, 34.662419969859556, 89.99925821464913 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinHEnd_Piv', t=( 7.598, 144.5391575953395, -206.00467602115208 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )

cmds.xform( 'R_FinH_upPiv', t=( 98.34687893282609, 134.06274677435147, -200.74126084190345 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinH01_Piv', t=( 7.597701436622621, 121.47801002727843, -190.0587481477165 ), ro=( -178.97197134064876, 34.662419969859556, 89.99925821464913 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinHEnd_Piv', t=( 7.598, 144.5391575953395, -206.00467602115208 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )


# ---------------------------------------------------------------------------------------
# use Sluggy fin rig creation command ( FK only ) to make ear rig
# L
L_FinHRigRet = denAR.den_makeFKappendageRig( side='L_', name='FinH', jointCount=1, radius=2, ctrlRadius=24.0, secondaryAxisOrient='zup' )
print( L_FinHRigRet )
L_FinHRigGrp = L_FinHRigRet[0]; print( L_FinHRigGrp )
L_FinHSpaceIN = L_FinHRigRet[1][0]; print( L_FinHSpaceIN )
L_FinHBindJnts = L_FinHRigRet[3]; print( L_FinHBindJnts )
L_FinHCtrls = L_FinHRigRet[4]; print( L_FinHCtrls )

denUt.den_connectProxyGeo( Jnts=L_FinHBindJnts )

L_FinHRigGrp = cmds.parent( L_FinHRigGrp, RootRigGrp )


L_FinHSpaceConstraint = cmds.parentConstraint( 'Tail02_Jnt', L_FinHSpaceIN, mo=True  )
L_FinHSpaceScaleConstraint = cmds.scaleConstraint( 'Tail02_Jnt', L_FinHSpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=L_FinHRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', L_FinHRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', L_FinHRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', L_FinHRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Left_Color', L_FinHRigGrp[0]+'.Ctrl_Color' )

# R
R_FinHRigRet = denAR.den_makeFKappendageRig( side='R_', name='FinH', jointCount=1, radius=2, ctrlRadius=24.0, secondaryAxisOrient='zup' )
print( R_FinHRigRet )
R_FinHRigGrp = R_FinHRigRet[0]; print( R_FinHRigGrp )
R_FinHSpaceIN = R_FinHRigRet[1][0]; print( R_FinHSpaceIN )
R_FinHBindJnts = R_FinHRigRet[3]; print( R_FinHBindJnts )
R_FinHCtrls = R_FinHRigRet[4]; print( R_FinHCtrls )

denUt.den_connectProxyGeo( Jnts=R_FinHBindJnts )

R_FinHRigGrp = cmds.parent( R_FinHRigGrp, RootRigGrp )

R_FinHSpaceConstraint = cmds.parentConstraint( 'Tail02_Jnt', R_FinHSpaceIN, mo=True  )
R_FinHSpaceScaleConstraint = cmds.scaleConstraint( 'Tail02_Jnt', R_FinHSpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=R_FinHRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', R_FinHRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', R_FinHRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', R_FinHRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Right_Color', R_FinHRigGrp[0]+'.Ctrl_Color' )



####### -------------------------------
# spike sld I
# ---------------------------------------------------------------------------------------
# use Sluggy fin pivots creation command

FinIPivsRet = denAR.den_makeFKappendagePivs( side='L_', name='FinI', jointCount=1, radius=2 )
cmds.parent( FinIPivsRet, RootPivGrp ) # put torso pivits under main pivot group

FinIPivsRet = denAR.den_makeFKappendagePivs( side='R_', name='FinI', jointCount=1, radius=2 )
cmds.parent( FinIPivsRet, RootPivGrp ) # put torso pivits under main pivot group

# reposition pivots
cmds.xform( 'L_FinI_upPiv', t=( 98.34687893282609, 126.7090644022359, -239.79748499602817 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinI01_Piv', t=( 4.991004085690619, 120.49751904432966, -235.8149940186576 ), ro=( 178.96422420825513, 45.876751692158145, 89.99867693693187 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinIEnd_Piv', t=( 4.991302649067998, 133.42692645525378, -249.14627927089654 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )

cmds.xform( 'R_FinI_upPiv', t=( 98.34687893282609, 126.7090644022359, -239.79748499602817 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinI01_Piv', t=( 4.991004085690619, 120.49751904432966, -235.8149940186576 ), ro=( 178.96422420825513, 45.876751692158145, 89.99867693693187 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinIEnd_Piv', t=( 4.991302649067998, 133.42692645525378, -249.14627927089654 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )


# ---------------------------------------------------------------------------------------
# use Sluggy fin rig creation command ( FK only ) to make ear rig
# L
L_FinIRigRet = denAR.den_makeFKappendageRig( side='L_', name='FinI', jointCount=1, radius=2, ctrlRadius=24.0, secondaryAxisOrient='zup' )
print( L_FinIRigRet )
L_FinIRigGrp = L_FinIRigRet[0]; print( L_FinIRigGrp )
L_FinISpaceIN = L_FinIRigRet[1][0]; print( L_FinISpaceIN )
L_FinIBindJnts = L_FinIRigRet[3]; print( L_FinIBindJnts )
L_FinICtrls = L_FinIRigRet[4]; print( L_FinICtrls )

denUt.den_connectProxyGeo( Jnts=L_FinIBindJnts )

L_FinIRigGrp = cmds.parent( L_FinIRigGrp, RootRigGrp )


L_FinISpaceConstraint = cmds.parentConstraint( 'Tail03_Jnt', L_FinISpaceIN, mo=True  )
L_FinISpaceScaleConstraint = cmds.scaleConstraint( 'Tail03_Jnt', L_FinISpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=L_FinIRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', L_FinIRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', L_FinIRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', L_FinIRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Left_Color', L_FinIRigGrp[0]+'.Ctrl_Color' )

# R
R_FinIRigRet = denAR.den_makeFKappendageRig( side='R_', name='FinI', jointCount=1, radius=2, ctrlRadius=24.0, secondaryAxisOrient='zup' )
print( R_FinIRigRet )
R_FinIRigGrp = R_FinIRigRet[0]; print( R_FinIRigGrp )
R_FinISpaceIN = R_FinIRigRet[1][0]; print( R_FinISpaceIN )
R_FinIBindJnts = R_FinIRigRet[3]; print( R_FinIBindJnts )
R_FinICtrls = R_FinIRigRet[4]; print( R_FinICtrls )

denUt.den_connectProxyGeo( Jnts=R_FinIBindJnts )

R_FinIRigGrp = cmds.parent( R_FinIRigGrp, RootRigGrp )

R_FinISpaceConstraint = cmds.parentConstraint( 'Tail03_Jnt', R_FinISpaceIN, mo=True  )
R_FinISpaceScaleConstraint = cmds.scaleConstraint( 'Tail03_Jnt', R_FinISpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=R_FinIRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', R_FinIRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', R_FinIRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', R_FinIRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Right_Color', R_FinIRigGrp[0]+'.Ctrl_Color' )

###################
######## ============================= Make Arm Spikes =========================================
####### -------------------------------
# spike arm A
# ---------------------------------------------------------------------------------------
# use Sluggy fin pivots creation command

FinArmAPivsRet = denAR.den_makeFKappendagePivs( side='L_', name='FinArmA', jointCount=1, radius=2 )
cmds.parent( FinArmAPivsRet, RootPivGrp ) # put torso pivits under main pivot group

FinArmAPivsRet = denAR.den_makeFKappendagePivs( side='R_', name='FinArmA', jointCount=1, radius=2 )
cmds.parent( FinArmAPivsRet, RootPivGrp ) # put torso pivits under main pivot group

# reposition pivots
cmds.xform( 'L_FinArmA_upPiv', t=( 122.41998538257761, 83.7256165022041, 36.72452421246382 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinArmA01_Piv', t=( 41.99064254760742, 80.99705505371094, 35.554847717285156 ), ro=( 177.88459457764353, 68.35573123173401, 89.99750282813955 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinArmAEnd_Piv', t=( 41.991, 89.19853841279061, 14.886934581477055 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )

cmds.xform( 'R_FinArmA_upPiv', t=( 122.41998538257761, 83.7256165022041, 36.72452421246382 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinArmA01_Piv', t=( 41.99064254760742, 80.99705505371094, 35.554847717285156 ), ro=( 177.88459457764353, 68.35573123173401, 89.99750282813955 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinArmAEnd_Piv', t=( 41.991, 89.19853841279061, 14.886934581477055 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )


# ---------------------------------------------------------------------------------------
# use Sluggy fin rig creation command ( FK only ) to make ear rig
# L
L_FinArmARigRet = denAR.den_makeFKappendageRig( side='L_', name='FinArmA', jointCount=1, radius=2, ctrlRadius=10.0, secondaryAxisOrient='zup' )
print( L_FinArmARigRet )
L_FinArmARigGrp = L_FinArmARigRet[0]; print( L_FinArmARigGrp )
L_FinArmASpaceIN = L_FinArmARigRet[1][0]; print( L_FinArmASpaceIN )
L_FinArmABindJnts = L_FinArmARigRet[3]; print( L_FinArmABindJnts )
L_FinArmACtrls = L_FinArmARigRet[4]; print( L_FinArmACtrls )

denUt.den_connectProxyGeo( Jnts=L_FinArmABindJnts )

L_FinArmARigGrp = cmds.parent( L_FinArmARigGrp, RootRigGrp )


L_FinArmASpaceConstraint = cmds.parentConstraint( 'L_Elbow_Jx', L_FinArmASpaceIN, mo=True  )
L_FinArmASpaceScaleConstraint = cmds.scaleConstraint( 'L_Elbow_Jx', L_FinArmASpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=L_FinArmARigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', L_FinArmARigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', L_FinArmARigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', L_FinArmARigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Left_Color', L_FinArmARigGrp[0]+'.Ctrl_Color' )

# R
R_FinArmARigRet = denAR.den_makeFKappendageRig( side='R_', name='FinArmA', jointCount=1, radius=2, ctrlRadius=10.0, secondaryAxisOrient='zup' )
print( R_FinArmARigRet )
R_FinArmARigGrp = R_FinArmARigRet[0]; print( R_FinArmARigGrp )
R_FinArmASpaceIN = R_FinArmARigRet[1][0]; print( R_FinArmASpaceIN )
R_FinArmABindJnts = R_FinArmARigRet[3]; print( R_FinArmABindJnts )
R_FinArmACtrls = R_FinArmARigRet[4]; print( R_FinArmACtrls )

denUt.den_connectProxyGeo( Jnts=R_FinArmABindJnts )

R_FinArmARigGrp = cmds.parent( R_FinArmARigGrp, RootRigGrp )

R_FinArmASpaceConstraint = cmds.parentConstraint( 'R_Elbow_Jx', R_FinArmASpaceIN, mo=True  )
R_FinArmASpaceScaleConstraint = cmds.scaleConstraint( 'R_Elbow_Jx', R_FinArmASpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=R_FinArmARigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', R_FinArmARigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', R_FinArmARigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', R_FinArmARigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Right_Color', R_FinArmARigGrp[0]+'.Ctrl_Color' )


####### -------------------------------
# spike arm B
# ---------------------------------------------------------------------------------------
# use Sluggy fin pivots creation command

FinArmBPivsRet = denAR.den_makeFKappendagePivs( side='L_', name='FinArmB', jointCount=1, radius=2 )
cmds.parent( FinArmBPivsRet, RootPivGrp ) # put torso pivits under main pivot group

FinArmBPivsRet = denAR.den_makeFKappendagePivs( side='R_', name='FinArmB', jointCount=1, radius=2 )
cmds.parent( FinArmBPivsRet, RootPivGrp ) # put torso pivits under main pivot group

# reposition pivots
cmds.xform( 'L_FinArmB_upPiv', t=( 122.41998538257761, 71.51645478794977, 37.81834956522577 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinArmB01_Piv', t=( 41.99064254760742, 68.7878933394566, 43.694288860121375 ), ro=( 179.47178536958384, 71.6399257767168, 89.99798252505992 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinArmBEnd_Piv', t=( 41.991, 78.93945113900746, 13.106431831481633 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )

cmds.xform( 'R_FinArmB_upPiv', t=( 122.41998538257761, 71.51645478794977, 37.81834956522577 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinArmB01_Piv', t=( 41.99064254760742, 68.7878933394566, 43.694288860121375 ), ro=( 179.47178536958384, 71.6399257767168, 89.99798252505992 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinArmBEnd_Piv', t=( 41.991, 78.93945113900746, 13.106431831481633 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )


# ---------------------------------------------------------------------------------------
# use Sluggy fin rig creation command ( FK only ) to make ear rig
# L
L_FinArmBRigRet = denAR.den_makeFKappendageRig( side='L_', name='FinArmB', jointCount=1, radius=2, ctrlRadius=10.0, secondaryAxisOrient='zup' )
print( L_FinArmBRigRet )
L_FinArmBRigGrp = L_FinArmBRigRet[0]; print( L_FinArmBRigGrp )
L_FinArmBSpaceIN = L_FinArmBRigRet[1][0]; print( L_FinArmBSpaceIN )
L_FinArmBBindJnts = L_FinArmBRigRet[3]; print( L_FinArmBBindJnts )
L_FinArmBCtrls = L_FinArmBRigRet[4]; print( L_FinArmBCtrls )

denUt.den_connectProxyGeo( Jnts=L_FinArmBBindJnts )

L_FinArmBRigGrp = cmds.parent( L_FinArmBRigGrp, RootRigGrp )


L_FinArmBSpaceConstraint = cmds.parentConstraint( 'L_Elbow_Jx', L_FinArmBSpaceIN, mo=True  )
L_FinArmBSpaceScaleConstraint = cmds.scaleConstraint( 'L_Elbow_Jx', L_FinArmBSpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=L_FinArmBRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', L_FinArmBRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', L_FinArmBRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', L_FinArmBRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Left_Color', L_FinArmBRigGrp[0]+'.Ctrl_Color' )

# R
R_FinArmBRigRet = denAR.den_makeFKappendageRig( side='R_', name='FinArmB', jointCount=1, radius=2, ctrlRadius=10.0, secondaryAxisOrient='zup' )
print( R_FinArmBRigRet )
R_FinArmBRigGrp = R_FinArmBRigRet[0]; print( R_FinArmBRigGrp )
R_FinArmBSpaceIN = R_FinArmBRigRet[1][0]; print( R_FinArmBSpaceIN )
R_FinArmBBindJnts = R_FinArmBRigRet[3]; print( R_FinArmBBindJnts )
R_FinArmBCtrls = R_FinArmBRigRet[4]; print( R_FinArmBCtrls )

denUt.den_connectProxyGeo( Jnts=R_FinArmBBindJnts )

R_FinArmBRigGrp = cmds.parent( R_FinArmBRigGrp, RootRigGrp )

R_FinArmBSpaceConstraint = cmds.parentConstraint( 'R_Elbow_Jx', R_FinArmBSpaceIN, mo=True  )
R_FinArmBSpaceScaleConstraint = cmds.scaleConstraint( 'R_Elbow_Jx', R_FinArmBSpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=R_FinArmBRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', R_FinArmBRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', R_FinArmBRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', R_FinArmBRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Right_Color', R_FinArmBRigGrp[0]+'.Ctrl_Color' )



####### -------------------------------
# spike arm C
# ---------------------------------------------------------------------------------------
# use Sluggy fin pivots creation command

FinArmCPivsRet = denAR.den_makeFKappendagePivs( side='L_', name='FinArmC', jointCount=1, radius=2 )
cmds.parent( FinArmCPivsRet, RootPivGrp ) # put torso pivits under main pivot group

FinArmCPivsRet = denAR.den_makeFKappendagePivs( side='R_', name='FinArmC', jointCount=1, radius=2 )
cmds.parent( FinArmCPivsRet, RootPivGrp ) # put torso pivits under main pivot group

# reposition pivots
cmds.xform( 'L_FinArmC_upPiv', t=( 122.41998538257761, 57.520930322664654, 43.86441613422895 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinArmC01_Piv', t=( 41.99064254760742, 54.79236887417149, 49.74035542912455 ), ro=( 178.51913061996018, 83.7186615161802, 89.99287357955777 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinArmCEnd_Piv', t=( 41.991, 57.66625395177407, 23.63106622937603 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )

cmds.xform( 'R_FinArmC_upPiv', t=( 122.41998538257761, 57.520930322664654, 43.86441613422895 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinArmC01_Piv', t=( 41.99064254760742, 54.79236887417149, 49.74035542912455 ), ro=( 178.51913061996018, 83.7186615161802, 89.99287357955777 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinArmCEnd_Piv', t=( 41.991, 57.66625395177407, 23.63106622937603 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )


# ---------------------------------------------------------------------------------------
# use Sluggy fin rig creation command ( FK only ) to make ear rig
# L
L_FinArmCRigRet = denAR.den_makeFKappendageRig( side='L_', name='FinArmC', jointCount=1, radius=2, ctrlRadius=10.0, secondaryAxisOrient='zup' )
print( L_FinArmCRigRet )
L_FinArmCRigGrp = L_FinArmCRigRet[0]; print( L_FinArmCRigGrp )
L_FinArmCSpaceIN = L_FinArmCRigRet[1][0]; print( L_FinArmCSpaceIN )
L_FinArmCBindJnts = L_FinArmCRigRet[3]; print( L_FinArmCBindJnts )
L_FinArmCCtrls = L_FinArmCRigRet[4]; print( L_FinArmCCtrls )

denUt.den_connectProxyGeo( Jnts=L_FinArmCBindJnts )

L_FinArmCRigGrp = cmds.parent( L_FinArmCRigGrp, RootRigGrp )


L_FinArmCSpaceConstraint = cmds.parentConstraint( 'L_Elbow_Jx', L_FinArmCSpaceIN, mo=True  )
L_FinArmCSpaceScaleConstraint = cmds.scaleConstraint( 'L_Elbow_Jx', L_FinArmCSpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=L_FinArmCRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', L_FinArmCRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', L_FinArmCRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', L_FinArmCRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Left_Color', L_FinArmCRigGrp[0]+'.Ctrl_Color' )

# R
R_FinArmCRigRet = denAR.den_makeFKappendageRig( side='R_', name='FinArmC', jointCount=1, radius=2, ctrlRadius=10.0, secondaryAxisOrient='zup' )
print( R_FinArmCRigRet )
R_FinArmCRigGrp = R_FinArmCRigRet[0]; print( R_FinArmCRigGrp )
R_FinArmCSpaceIN = R_FinArmCRigRet[1][0]; print( R_FinArmCSpaceIN )
R_FinArmCBindJnts = R_FinArmCRigRet[3]; print( R_FinArmCBindJnts )
R_FinArmCCtrls = R_FinArmCRigRet[4]; print( R_FinArmCCtrls )

denUt.den_connectProxyGeo( Jnts=R_FinArmCBindJnts )

R_FinArmCRigGrp = cmds.parent( R_FinArmCRigGrp, RootRigGrp )

R_FinArmCSpaceConstraint = cmds.parentConstraint( 'R_Elbow_Jx', R_FinArmCSpaceIN, mo=True  )
R_FinArmCSpaceScaleConstraint = cmds.scaleConstraint( 'R_Elbow_Jx', R_FinArmCSpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=R_FinArmCRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', R_FinArmCRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', R_FinArmCRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', R_FinArmCRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Right_Color', R_FinArmCRigGrp[0]+'.Ctrl_Color' )


####### -------------------------------
# spike arm D
# ---------------------------------------------------------------------------------------
# use Sluggy fin pivots creation command

FinArmDPivsRet = denAR.den_makeFKappendagePivs( side='L_', name='FinArmD', jointCount=1, radius=2 )
cmds.parent( FinArmDPivsRet, RootPivGrp ) # put torso pivits under main pivot group

FinArmDPivsRet = denAR.den_makeFKappendagePivs( side='R_', name='FinArmD', jointCount=1, radius=2 )
cmds.parent( FinArmDPivsRet, RootPivGrp ) # put torso pivits under main pivot group

# reposition pivots
cmds.xform( 'L_FinArmD_upPiv', t=( 119.22341679444986, 40.67831890635914, 51.529963637803895 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinArmD01_Piv', t=( 38.7940739594797, 37.94975745786597, 57.4059029326995 ), ro=( 177.99505576983063, 89.24504193919336, 89.88280031384177 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinArmDEnd_Piv', t=( 38.794431411872274, 38.124506090547804, 44.14450321077379 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )

cmds.xform( 'R_FinArmD_upPiv', t=( 119.22341679444986, 40.67831890635914, 51.529963637803895 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinArmD01_Piv', t=( 38.7940739594797, 37.94975745786597, 57.4059029326995 ), ro=( 177.99505576983063, 89.24504193919336, 89.88280031384177 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinArmDEnd_Piv', t=( 38.794431411872274, 38.124506090547804, 44.14450321077379 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )


# ---------------------------------------------------------------------------------------
# use Sluggy fin rig creation command ( FK only ) to make ear rig
# L
L_FinArmDRigRet = denAR.den_makeFKappendageRig( side='L_', name='FinArmD', jointCount=1, radius=2, ctrlRadius=10.0, secondaryAxisOrient='zup' )
print( L_FinArmDRigRet )
L_FinArmDRigGrp = L_FinArmDRigRet[0]; print( L_FinArmDRigGrp )
L_FinArmDSpaceIN = L_FinArmDRigRet[1][0]; print( L_FinArmDSpaceIN )
L_FinArmDBindJnts = L_FinArmDRigRet[3]; print( L_FinArmDBindJnts )
L_FinArmDCtrls = L_FinArmDRigRet[4]; print( L_FinArmDCtrls )

denUt.den_connectProxyGeo( Jnts=L_FinArmDBindJnts )

L_FinArmDRigGrp = cmds.parent( L_FinArmDRigGrp, RootRigGrp )


L_FinArmDSpaceConstraint = cmds.parentConstraint( 'L_Elbow_Jx', L_FinArmDSpaceIN, mo=True  )
L_FinArmDSpaceScaleConstraint = cmds.scaleConstraint( 'L_Elbow_Jx', L_FinArmDSpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=L_FinArmDRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', L_FinArmDRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', L_FinArmDRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', L_FinArmDRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Left_Color', L_FinArmDRigGrp[0]+'.Ctrl_Color' )

# R
R_FinArmDRigRet = denAR.den_makeFKappendageRig( side='R_', name='FinArmD', jointCount=1, radius=2, ctrlRadius=10.0, secondaryAxisOrient='zup' )
print( R_FinArmDRigRet )
R_FinArmDRigGrp = R_FinArmDRigRet[0]; print( R_FinArmDRigGrp )
R_FinArmDSpaceIN = R_FinArmDRigRet[1][0]; print( R_FinArmDSpaceIN )
R_FinArmDBindJnts = R_FinArmDRigRet[3]; print( R_FinArmDBindJnts )
R_FinArmDCtrls = R_FinArmDRigRet[4]; print( R_FinArmDCtrls )

denUt.den_connectProxyGeo( Jnts=R_FinArmDBindJnts )

R_FinArmDRigGrp = cmds.parent( R_FinArmDRigGrp, RootRigGrp )

R_FinArmDSpaceConstraint = cmds.parentConstraint( 'R_Elbow_Jx', R_FinArmDSpaceIN, mo=True  )
R_FinArmDSpaceScaleConstraint = cmds.scaleConstraint( 'R_Elbow_Jx', R_FinArmDSpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=R_FinArmDRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', R_FinArmDRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', R_FinArmDRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', R_FinArmDRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Right_Color', R_FinArmDRigGrp[0]+'.Ctrl_Color' )


###################
######## ============================= Make Leg SPIKE =========================================
####### -------------------------------
# spike leg A
# ---------------------------------------------------------------------------------------
# use Sluggy fin pivots creation command

FinLegAPivsRet = denAR.den_makeFKappendagePivs( side='L_', name='FinLegA', jointCount=1, radius=2 )
cmds.parent( FinLegAPivsRet, RootPivGrp ) # put torso pivits under main pivot group

FinLegAPivsRet = denAR.den_makeFKappendagePivs( side='R_', name='FinLegA', jointCount=1, radius=2 )
cmds.parent( FinLegAPivsRet, RootPivGrp ) # put torso pivits under main pivot group

# reposition pivots
cmds.xform( 'L_FinLegA_upPiv', t=( 107.99306953019641, 121.72895036135321, -103.84943223043017 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinLegA01_Piv', t=( 27.135849303267648, 117.90846904527697, -105.48565639950593 ), ro=( 177.06515599421286, 62.27251226707198, 89.99816989662848 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinLegAEnd_Piv', t=( 27.136206755660226, 129.09937431490292, -126.77636576667783 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )

cmds.xform( 'R_FinLegA_upPiv', t=( 107.99306953019641, 121.72895036135321, -103.84943223043017 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinLegA01_Piv', t=( 27.135849303267648, 117.90846904527697, -105.48565639950593 ), ro=( 177.06515599421286, 62.27251226707198, 89.99816989662848 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinLegAEnd_Piv', t=( 27.136206755660226, 129.09937431490292, -126.77636576667783 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )


# ---------------------------------------------------------------------------------------
# use Sluggy fin rig creation command ( FK only ) to make ear rig
# L
L_FinLegARigRet = denAR.den_makeFKappendageRig( side='L_', name='FinLegA', jointCount=1, radius=2, ctrlRadius=10.0, secondaryAxisOrient='zup' )
print( L_FinLegARigRet )
L_FinLegARigGrp = L_FinLegARigRet[0]; print( L_FinLegARigGrp )
L_FinLegASpaceIN = L_FinLegARigRet[1][0]; print( L_FinLegASpaceIN )
L_FinLegABindJnts = L_FinLegARigRet[3]; print( L_FinLegABindJnts )
L_FinLegACtrls = L_FinLegARigRet[4]; print( L_FinLegACtrls )

denUt.den_connectProxyGeo( Jnts=L_FinLegABindJnts )

L_FinLegARigGrp = cmds.parent( L_FinLegARigGrp, RootRigGrp )


L_FinLegASpaceConstraint = cmds.parentConstraint( 'L_Hip_Jx', L_FinLegASpaceIN, mo=True  )
L_FinLegASpaceScaleConstraint = cmds.scaleConstraint( 'L_Hip_Jx', L_FinLegASpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=L_FinLegARigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', L_FinLegARigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', L_FinLegARigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', L_FinLegARigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Left_Color', L_FinLegARigGrp[0]+'.Ctrl_Color' )

# R
R_FinLegARigRet = denAR.den_makeFKappendageRig( side='R_', name='FinLegA', jointCount=1, radius=2, ctrlRadius=10.0, secondaryAxisOrient='zup' )
print( R_FinLegARigRet )
R_FinLegARigGrp = R_FinLegARigRet[0]; print( R_FinLegARigGrp )
R_FinLegASpaceIN = R_FinLegARigRet[1][0]; print( R_FinLegASpaceIN )
R_FinLegABindJnts = R_FinLegARigRet[3]; print( R_FinLegABindJnts )
R_FinLegACtrls = R_FinLegARigRet[4]; print( R_FinLegACtrls )

denUt.den_connectProxyGeo( Jnts=R_FinLegABindJnts )

R_FinLegARigGrp = cmds.parent( R_FinLegARigGrp, RootRigGrp )

R_FinLegASpaceConstraint = cmds.parentConstraint( 'R_Hip_Jx', R_FinLegASpaceIN, mo=True  )
R_FinLegASpaceScaleConstraint = cmds.scaleConstraint( 'R_Hip_Jx', R_FinLegASpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=R_FinLegARigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', R_FinLegARigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', R_FinLegARigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', R_FinLegARigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Right_Color', R_FinLegARigGrp[0]+'.Ctrl_Color' )



####### -------------------------------
# spike leg B
# ---------------------------------------------------------------------------------------
# use Sluggy fin pivots creation command

FinLegBPivsRet = denAR.den_makeFKappendagePivs( side='L_', name='FinLegB', jointCount=1, radius=2 )
cmds.parent( FinLegBPivsRet, RootPivGrp ) # put torso pivits under main pivot group

FinLegBPivsRet = denAR.den_makeFKappendagePivs( side='R_', name='FinLegB', jointCount=1, radius=2 )
cmds.parent( FinLegBPivsRet, RootPivGrp ) # put torso pivits under main pivot group

# reposition pivots
cmds.xform( 'L_FinLegB_upPiv', t=( 107.99306953019641, 98.51437979016987, -96.4775697097129 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinLegB01_Piv', t=( 35.71345699319904, 100.23783700184647, -98.81105563055684 ), ro=( 1.6938641186790577, 79.17515821335535, -89.99481740467094 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinLegBEnd_Piv', t=( 35.713814445591616, 96.28604989223572, -119.47836196887424 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )

cmds.xform( 'R_FinLegB_upPiv', t=( 107.99306953019641, 98.51437979016987, -96.4775697097129 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinLegB01_Piv', t=( 35.71345699319904, 100.23783700184647, -98.81105563055684 ), ro=( 1.6938641186790577, 79.17515821335535, -89.99481740467094 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinLegBEnd_Piv', t=( 35.713814445591616, 96.28604989223572, -119.47836196887424 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )

# ---------------------------------------------------------------------------------------
# use Sluggy fin rig creation command ( FK only ) to make ear rig
# L
L_FinLegBRigRet = denAR.den_makeFKappendageRig( side='L_', name='FinLegB', jointCount=1, radius=2, ctrlRadius=10.0, secondaryAxisOrient='zup' )
print( L_FinLegBRigRet )
L_FinLegBRigGrp = L_FinLegBRigRet[0]; print( L_FinLegBRigGrp )
L_FinLegBSpaceIN = L_FinLegBRigRet[1][0]; print( L_FinLegBSpaceIN )
L_FinLegBBindJnts = L_FinLegBRigRet[3]; print( L_FinLegBBindJnts )
L_FinLegBCtrls = L_FinLegBRigRet[4]; print( L_FinLegBCtrls )

denUt.den_connectProxyGeo( Jnts=L_FinLegBBindJnts )

L_FinLegBRigGrp = cmds.parent( L_FinLegBRigGrp, RootRigGrp )


L_FinLegBSpaceConstraint = cmds.parentConstraint( 'L_Hip_Jx', L_FinLegBSpaceIN, mo=True  )
L_FinLegBSpaceScaleConstraint = cmds.scaleConstraint( 'L_Hip_Jx', L_FinLegBSpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=L_FinLegBRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', L_FinLegBRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', L_FinLegBRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', L_FinLegBRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Left_Color', L_FinLegBRigGrp[0]+'.Ctrl_Color' )

# R
R_FinLegBRigRet = denAR.den_makeFKappendageRig( side='R_', name='FinLegB', jointCount=1, radius=2, ctrlRadius=10.0, secondaryAxisOrient='zup' )
print( R_FinLegBRigRet )
R_FinLegBRigGrp = R_FinLegBRigRet[0]; print( R_FinLegBRigGrp )
R_FinLegBSpaceIN = R_FinLegBRigRet[1][0]; print( R_FinLegBSpaceIN )
R_FinLegBBindJnts = R_FinLegBRigRet[3]; print( R_FinLegBBindJnts )
R_FinLegBCtrls = R_FinLegBRigRet[4]; print( R_FinLegBCtrls )

denUt.den_connectProxyGeo( Jnts=R_FinLegBBindJnts )

R_FinLegBRigGrp = cmds.parent( R_FinLegBRigGrp, RootRigGrp )

R_FinLegBSpaceConstraint = cmds.parentConstraint( 'R_Hip_Jx', R_FinLegBSpaceIN, mo=True  )
R_FinLegBSpaceScaleConstraint = cmds.scaleConstraint( 'R_Hip_Jx', R_FinLegBSpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=R_FinLegBRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', R_FinLegBRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', R_FinLegBRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', R_FinLegBRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Right_Color', R_FinLegBRigGrp[0]+'.Ctrl_Color' )



####### -------------------------------
# spike leg C
# ---------------------------------------------------------------------------------------
# use Sluggy fin pivots creation command

FinLegCPivsRet = denAR.den_makeFKappendagePivs( side='L_', name='FinLegC', jointCount=1, radius=2 )
cmds.parent( FinLegCPivsRet, RootPivGrp ) # put torso pivits under main pivot group

FinLegCPivsRet = denAR.den_makeFKappendagePivs( side='R_', name='FinLegC', jointCount=1, radius=2 )
cmds.parent( FinLegCPivsRet, RootPivGrp ) # put torso pivits under main pivot group

# reposition pivots
cmds.xform( 'L_FinLegC_upPiv', t=( 111.19525499433777, 86.01105511635838, -80.23245770800635 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinLegC01_Piv', t=( 38.91564245734038, 87.73451232803498, -82.56594362885029 ), ro=( 1.6938641186790577, 79.17515821335535, -89.99481740467094 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinLegCEnd_Piv', t=( 38.91599990973296, 83.78272521842423, -103.2332499671677 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )

cmds.xform( 'R_FinLegC_upPiv', t=( 111.19525499433777, 86.01105511635838, -80.23245770800635 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinLegC01_Piv', t=( 38.91564245734038, 87.73451232803498, -82.56594362885029 ), ro=( 1.6938641186790577, 79.17515821335535, -89.99481740467094 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinLegCEnd_Piv', t=( 38.91599990973296, 83.78272521842423, -103.2332499671677 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )

# ---------------------------------------------------------------------------------------
# use Sluggy fin rig creation command ( FK only ) to make ear rig
# L
L_FinLegCRigRet = denAR.den_makeFKappendageRig( side='L_', name='FinLegC', jointCount=1, radius=2, ctrlRadius=10.0, secondaryAxisOrient='zup' )
print( L_FinLegCRigRet )
L_FinLegCRigGrp = L_FinLegCRigRet[0]; print( L_FinLegCRigGrp )
L_FinLegCSpaceIN = L_FinLegCRigRet[1][0]; print( L_FinLegCSpaceIN )
L_FinLegCBindJnts = L_FinLegCRigRet[3]; print( L_FinLegCBindJnts )
L_FinLegCCtrls = L_FinLegCRigRet[4]; print( L_FinLegCCtrls )

denUt.den_connectProxyGeo( Jnts=L_FinLegCBindJnts )

L_FinLegCRigGrp = cmds.parent( L_FinLegCRigGrp, RootRigGrp )


L_FinLegCSpaceConstraint = cmds.parentConstraint( 'L_Hip_Jx', L_FinLegCSpaceIN, mo=True  )
L_FinLegCSpaceScaleConstraint = cmds.scaleConstraint( 'L_Hip_Jx', L_FinLegCSpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=L_FinLegCRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', L_FinLegCRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', L_FinLegCRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', L_FinLegCRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Left_Color', L_FinLegCRigGrp[0]+'.Ctrl_Color' )

# R
R_FinLegCRigRet = denAR.den_makeFKappendageRig( side='R_', name='FinLegC', jointCount=1, radius=2, ctrlRadius=10.0, secondaryAxisOrient='zup' )
print( R_FinLegCRigRet )
R_FinLegCRigGrp = R_FinLegCRigRet[0]; print( R_FinLegCRigGrp )
R_FinLegCSpaceIN = R_FinLegCRigRet[1][0]; print( R_FinLegCSpaceIN )
R_FinLegCBindJnts = R_FinLegCRigRet[3]; print( R_FinLegCBindJnts )
R_FinLegCCtrls = R_FinLegCRigRet[4]; print( R_FinLegCCtrls )

denUt.den_connectProxyGeo( Jnts=R_FinLegCBindJnts )

R_FinLegCRigGrp = cmds.parent( R_FinLegCRigGrp, RootRigGrp )

R_FinLegCSpaceConstraint = cmds.parentConstraint( 'R_Hip_Jx', R_FinLegCSpaceIN, mo=True  )
R_FinLegCSpaceScaleConstraint = cmds.scaleConstraint( 'R_Hip_Jx', R_FinLegCSpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=R_FinLegCRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', R_FinLegCRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', R_FinLegCRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', R_FinLegCRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Right_Color', R_FinLegCRigGrp[0]+'.Ctrl_Color' )


####### -------------------------------
# spike leg D
# ---------------------------------------------------------------------------------------
# use Sluggy fin pivots creation command

FinLegDPivsRet = denAR.den_makeFKappendagePivs( side='L_', name='FinLegD', jointCount=1, radius=2 )
cmds.parent( FinLegDPivsRet, RootPivGrp ) # put torso pivits under main pivot group

FinLegDPivsRet = denAR.den_makeFKappendagePivs( side='R_', name='FinLegD', jointCount=1, radius=2 )
cmds.parent( FinLegDPivsRet, RootPivGrp ) # put torso pivits under main pivot group

# reposition pivots
cmds.xform( 'L_FinLegD_upPiv', t=( 111.19525499433777, 71.55343704216823, -89.58229454640477 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinLegD01_Piv', t=( 39.73254671279812, 73.27689425384483, -91.91578046724871 ), ro=( 179.20554229741214, 33.61453726661717, 89.99741036675911 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinLegDEnd_Piv', t=( 39.732904165190696, 81.18554831886911, -97.17317053487243 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )

cmds.xform( 'R_FinLegD_upPiv', t=( 111.19525499433777, 71.55343704216823, -89.58229454640477 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinLegD01_Piv', t=( 39.73254671279812, 73.27689425384483, -91.91578046724871 ), ro=( 179.20554229741214, 33.61453726661717, 89.99741036675911 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinLegDEnd_Piv', t=( 39.732904165190696, 81.18554831886911, -97.17317053487243 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )

# ---------------------------------------------------------------------------------------
# use Sluggy fin rig creation command ( FK only ) to make ear rig
# L
L_FinLegDRigRet = denAR.den_makeFKappendageRig( side='L_', name='FinLegD', jointCount=1, radius=2, ctrlRadius=10.0, secondaryAxisOrient='zup' )
print( L_FinLegDRigRet )
L_FinLegDRigGrp = L_FinLegDRigRet[0]; print( L_FinLegDRigGrp )
L_FinLegDSpaceIN = L_FinLegDRigRet[1][0]; print( L_FinLegDSpaceIN )
L_FinLegDBindJnts = L_FinLegDRigRet[3]; print( L_FinLegDBindJnts )
L_FinLegDCtrls = L_FinLegDRigRet[4]; print( L_FinLegDCtrls )

denUt.den_connectProxyGeo( Jnts=L_FinLegDBindJnts )

L_FinLegDRigGrp = cmds.parent( L_FinLegDRigGrp, RootRigGrp )


L_FinLegDSpaceConstraint = cmds.parentConstraint( 'L_Knee_Jx', L_FinLegDSpaceIN, mo=True  )
L_FinLegDSpaceScaleConstraint = cmds.scaleConstraint( 'L_Knee_Jx', L_FinLegDSpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=L_FinLegDRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', L_FinLegDRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', L_FinLegDRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', L_FinLegDRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Left_Color', L_FinLegDRigGrp[0]+'.Ctrl_Color' )

# R
R_FinLegDRigRet = denAR.den_makeFKappendageRig( side='R_', name='FinLegD', jointCount=1, radius=2, ctrlRadius=10.0, secondaryAxisOrient='zup' )
print( R_FinLegDRigRet )
R_FinLegDRigGrp = R_FinLegDRigRet[0]; print( R_FinLegDRigGrp )
R_FinLegDSpaceIN = R_FinLegDRigRet[1][0]; print( R_FinLegDSpaceIN )
R_FinLegDBindJnts = R_FinLegDRigRet[3]; print( R_FinLegDBindJnts )
R_FinLegDCtrls = R_FinLegDRigRet[4]; print( R_FinLegDCtrls )

denUt.den_connectProxyGeo( Jnts=R_FinLegDBindJnts )

R_FinLegDRigGrp = cmds.parent( R_FinLegDRigGrp, RootRigGrp )

R_FinLegDSpaceConstraint = cmds.parentConstraint( 'R_Knee_Jx', R_FinLegDSpaceIN, mo=True  )
R_FinLegDSpaceScaleConstraint = cmds.scaleConstraint( 'R_Knee_Jx', R_FinLegDSpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=R_FinLegDRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', R_FinLegDRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', R_FinLegDRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', R_FinLegDRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Right_Color', R_FinLegDRigGrp[0]+'.Ctrl_Color' )



####### -------------------------------
# spike leg E
# ---------------------------------------------------------------------------------------
# use Sluggy fin pivots creation command

FinLegEPivsRet = denAR.den_makeFKappendagePivs( side='L_', name='FinLegE', jointCount=1, radius=2 )
cmds.parent( FinLegEPivsRet, RootPivGrp ) # put torso pivits under main pivot group

FinLegEPivsRet = denAR.den_makeFKappendagePivs( side='R_', name='FinLegE', jointCount=1, radius=2 )
cmds.parent( FinLegEPivsRet, RootPivGrp ) # put torso pivits under main pivot group

# reposition pivots
cmds.xform( 'L_FinLegE_upPiv', t=( 111.19525499433777, 63.67109208422215, -96.43650755331439 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinLegE01_Piv', t=( 39.73254671279812, 65.39454929589876, -98.76999347415833 ), ro=( 179.70800857960327, 46.3811973324997, 89.99766349034265 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinLegEEnd_Piv', t=( 39.732904165190696, 74.15997998678674, -107.96855602075509 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )

cmds.xform( 'R_FinLegE_upPiv', t=( 111.19525499433777, 63.67109208422215, -96.43650755331439 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinLegE01_Piv', t=( 39.73254671279812, 65.39454929589876, -98.76999347415833 ), ro=( 179.70800857960327, 46.3811973324997, 89.99766349034265 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinLegEEnd_Piv', t=( 39.732904165190696, 74.15997998678674, -107.96855602075509 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )

# ---------------------------------------------------------------------------------------
# use Sluggy fin rig creation command ( FK only ) to make ear rig
# L
L_FinLegERigRet = denAR.den_makeFKappendageRig( side='L_', name='FinLegE', jointCount=1, radius=2, ctrlRadius=10.0, secondaryAxisOrient='zup' )
print( L_FinLegERigRet )
L_FinLegERigGrp = L_FinLegERigRet[0]; print( L_FinLegERigGrp )
L_FinLegESpaceIN = L_FinLegERigRet[1][0]; print( L_FinLegESpaceIN )
L_FinLegEBindJnts = L_FinLegERigRet[3]; print( L_FinLegEBindJnts )
L_FinLegECtrls = L_FinLegERigRet[4]; print( L_FinLegECtrls )

denUt.den_connectProxyGeo( Jnts=L_FinLegEBindJnts )

L_FinLegERigGrp = cmds.parent( L_FinLegERigGrp, RootRigGrp )


L_FinLegESpaceConstraint = cmds.parentConstraint( 'L_Knee_Jx', L_FinLegESpaceIN, mo=True  )
L_FinLegESpaceScaleConstraint = cmds.scaleConstraint( 'L_Knee_Jx', L_FinLegESpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=L_FinLegERigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', L_FinLegERigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', L_FinLegERigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', L_FinLegERigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Left_Color', L_FinLegERigGrp[0]+'.Ctrl_Color' )

# R
R_FinLegERigRet = denAR.den_makeFKappendageRig( side='R_', name='FinLegE', jointCount=1, radius=2, ctrlRadius=10.0, secondaryAxisOrient='zup' )
print( R_FinLegERigRet )
R_FinLegERigGrp = R_FinLegERigRet[0]; print( R_FinLegERigGrp )
R_FinLegESpaceIN = R_FinLegERigRet[1][0]; print( R_FinLegESpaceIN )
R_FinLegEBindJnts = R_FinLegERigRet[3]; print( R_FinLegEBindJnts )
R_FinLegECtrls = R_FinLegERigRet[4]; print( R_FinLegECtrls )

denUt.den_connectProxyGeo( Jnts=R_FinLegEBindJnts )

R_FinLegERigGrp = cmds.parent( R_FinLegERigGrp, RootRigGrp )

R_FinLegESpaceConstraint = cmds.parentConstraint( 'R_Knee_Jx', R_FinLegESpaceIN, mo=True  )
R_FinLegESpaceScaleConstraint = cmds.scaleConstraint( 'R_Knee_Jx', R_FinLegESpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=R_FinLegERigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', R_FinLegERigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', R_FinLegERigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', R_FinLegERigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Right_Color', R_FinLegERigGrp[0]+'.Ctrl_Color' )


####### -------------------------------
# spike leg F
# ---------------------------------------------------------------------------------------
# use Sluggy fin pivots creation command

FinLegFPivsRet = denAR.den_makeFKappendagePivs( side='L_', name='FinLegF', jointCount=1, radius=2 )
cmds.parent( FinLegFPivsRet, RootPivGrp ) # put torso pivits under main pivot group

FinLegFPivsRet = denAR.den_makeFKappendagePivs( side='R_', name='FinLegF', jointCount=1, radius=2 )
cmds.parent( FinLegFPivsRet, RootPivGrp ) # put torso pivits under main pivot group

# reposition pivots
cmds.xform( 'L_FinLegF_upPiv', t=( 111.19525499433777, 53.56112789903045, -106.28943875074698 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinLegF01_Piv', t=( 33.840042728533504, 55.284585110707056, -108.62292467159092 ), ro=( -179.97130692664152, 54.358122518416806, 89.99807700835166 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinLegFEnd_Piv', t=( 33.84040018092608, 65.9349243784952, -123.47621294888813 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )

cmds.xform( 'R_FinLegF_upPiv', t=( 111.19525499433777, 53.56112789903045, -106.28943875074698 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinLegF01_Piv', t=( 33.840042728533504, 55.284585110707056, -108.62292467159092 ), ro=( -179.97130692664152, 54.358122518416806, 89.99807700835166 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinLegFEnd_Piv', t=( 33.84040018092608, 65.9349243784952, -123.47621294888813 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )

# ---------------------------------------------------------------------------------------
# use Sluggy fin rig creation command ( FK only ) to make ear rig
# L
L_FinLegFRigRet = denAR.den_makeFKappendageRig( side='L_', name='FinLegF', jointCount=1, radius=2, ctrlRadius=10.0, secondaryAxisOrient='zup' )
print( L_FinLegFRigRet )
L_FinLegFRigGrp = L_FinLegFRigRet[0]; print( L_FinLegFRigGrp )
L_FinLegFSpaceIN = L_FinLegFRigRet[1][0]; print( L_FinLegFSpaceIN )
L_FinLegFBindJnts = L_FinLegFRigRet[3]; print( L_FinLegFBindJnts )
L_FinLegFCtrls = L_FinLegFRigRet[4]; print( L_FinLegFCtrls )

denUt.den_connectProxyGeo( Jnts=L_FinLegFBindJnts )

L_FinLegFRigGrp = cmds.parent( L_FinLegFRigGrp, RootRigGrp )


L_FinLegFSpaceConstraint = cmds.parentConstraint( 'L_Knee_Jx', L_FinLegFSpaceIN, mo=True  )
L_FinLegFSpaceScaleConstraint = cmds.scaleConstraint( 'L_Knee_Jx', L_FinLegFSpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=L_FinLegFRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', L_FinLegFRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', L_FinLegFRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', L_FinLegFRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Left_Color', L_FinLegFRigGrp[0]+'.Ctrl_Color' )

# R
R_FinLegFRigRet = denAR.den_makeFKappendageRig( side='R_', name='FinLegF', jointCount=1, radius=2, ctrlRadius=10.0, secondaryAxisOrient='zup' )
print( R_FinLegFRigRet )
R_FinLegFRigGrp = R_FinLegFRigRet[0]; print( R_FinLegFRigGrp )
R_FinLegFSpaceIN = R_FinLegFRigRet[1][0]; print( R_FinLegFSpaceIN )
R_FinLegFBindJnts = R_FinLegFRigRet[3]; print( R_FinLegFBindJnts )
R_FinLegFCtrls = R_FinLegFRigRet[4]; print( R_FinLegFCtrls )

denUt.den_connectProxyGeo( Jnts=R_FinLegFBindJnts )

R_FinLegFRigGrp = cmds.parent( R_FinLegFRigGrp, RootRigGrp )

R_FinLegFSpaceConstraint = cmds.parentConstraint( 'R_Knee_Jx', R_FinLegFSpaceIN, mo=True  )
R_FinLegFSpaceScaleConstraint = cmds.scaleConstraint( 'R_Knee_Jx', R_FinLegFSpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=R_FinLegFRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', R_FinLegFRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', R_FinLegFRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', R_FinLegFRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Right_Color', R_FinLegFRigGrp[0]+'.Ctrl_Color' )



####### -------------------------------
# spike leg G
# ---------------------------------------------------------------------------------------
# use Sluggy fin pivots creation command

FinLegGPivsRet = denAR.den_makeFKappendagePivs( side='L_', name='FinLegG', jointCount=1, radius=2 )
cmds.parent( FinLegGPivsRet, RootPivGrp ) # put torso pivits under main pivot group

FinLegGPivsRet = denAR.den_makeFKappendagePivs( side='R_', name='FinLegG', jointCount=1, radius=2 )
cmds.parent( FinLegGPivsRet, RootPivGrp ) # put torso pivits under main pivot group

# reposition pivots
cmds.xform( 'L_FinLegG_upPiv', t=( 111.19525499433777, 46.16265294066672, -111.14089773983797 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinLegG01_Piv', t=( 33.840042728533504, 44.97523475888873, -113.47438366068191 ), ro=( 178.9304801843675, 83.81072135331233, 89.99102350979437 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_FinLegGEnd_Piv', t=( 33.84040018092608, 47.256807270494946, -134.5132821490701 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )

cmds.xform( 'R_FinLegG_upPiv', t=( 111.19525499433777, 46.16265294066672, -111.14089773983797 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinLegG01_Piv', t=( 33.840042728533504, 44.97523475888873, -113.47438366068191 ), ro=( 178.9304801843675, 83.81072135331233, 89.99102350979437 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_FinLegGEnd_Piv', t=( 33.84040018092608, 47.256807270494946, -134.5132821490701 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )

# ---------------------------------------------------------------------------------------
# use Sluggy fin rig creation command ( FK only ) to make ear rig
# L
L_FinLegGRigRet = denAR.den_makeFKappendageRig( side='L_', name='FinLegG', jointCount=1, radius=2, ctrlRadius=10.0, secondaryAxisOrient='zup' )
print( L_FinLegGRigRet )
L_FinLegGRigGrp = L_FinLegGRigRet[0]; print( L_FinLegGRigGrp )
L_FinLegGSpaceIN = L_FinLegGRigRet[1][0]; print( L_FinLegGSpaceIN )
L_FinLegGBindJnts = L_FinLegGRigRet[3]; print( L_FinLegGBindJnts )
L_FinLegGCtrls = L_FinLegGRigRet[4]; print( L_FinLegGCtrls )

denUt.den_connectProxyGeo( Jnts=L_FinLegGBindJnts )

L_FinLegGRigGrp = cmds.parent( L_FinLegGRigGrp, RootRigGrp )


L_FinLegGSpaceConstraint = cmds.parentConstraint( 'L_Hock_Jnt', L_FinLegGSpaceIN, mo=True  )
L_FinLegGSpaceScaleConstraint = cmds.scaleConstraint( 'L_Hock_Jnt', L_FinLegGSpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=L_FinLegGRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', L_FinLegGRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', L_FinLegGRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', L_FinLegGRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Left_Color', L_FinLegGRigGrp[0]+'.Ctrl_Color' )

# R
R_FinLegGRigRet = denAR.den_makeFKappendageRig( side='R_', name='FinLegG', jointCount=1, radius=2, ctrlRadius=10.0, secondaryAxisOrient='zup' )
print( R_FinLegGRigRet )
R_FinLegGRigGrp = R_FinLegGRigRet[0]; print( R_FinLegGRigGrp )
R_FinLegGSpaceIN = R_FinLegGRigRet[1][0]; print( R_FinLegGSpaceIN )
R_FinLegGBindJnts = R_FinLegGRigRet[3]; print( R_FinLegGBindJnts )
R_FinLegGCtrls = R_FinLegGRigRet[4]; print( R_FinLegGCtrls )

denUt.den_connectProxyGeo( Jnts=R_FinLegGBindJnts )

R_FinLegGRigGrp = cmds.parent( R_FinLegGRigGrp, RootRigGrp )

R_FinLegGSpaceConstraint = cmds.parentConstraint( 'R_Hock_Jnt', R_FinLegGSpaceIN, mo=True  )
R_FinLegGSpaceScaleConstraint = cmds.scaleConstraint( 'R_Hock_Jnt', R_FinLegGSpaceIN, mo=True  ) # need this because parentConstraint only does Translate/Rotate

denUt.den_AddSafetyCovers( rigGroup=R_FinLegGRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', R_FinLegGRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', R_FinLegGRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', R_FinLegGRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Right_Color', R_FinLegGRigGrp[0]+'.Ctrl_Color' )




###################
######## ============================= EYE =========================================
# ---------------------------------------------------------------------------------------
# create eyeball pivots

L_EyePivGrp = denBR.den_makeEyePiv( side='L_', radius=0.5 )
R_EyePivGrp = denBR.den_makeEyePiv( side='R_', radius=0.5 )

L_EyePivGrp = cmds.parent( L_EyePivGrp, RootPivGrp )
R_EyePivGrp = cmds.parent( R_EyePivGrp, RootPivGrp )


# put the pivots in the center of the eyeball geometry and lined up with the iris
cmds.xform( 'L_Eye_Piv', t=( 6.485136625973131, 207.31325998101738, 226.21829151157678 ), ro=( 5.939935635096861, 1.8369896653334559, 5.922171239648797 ), s=( 1.0, 1.0, 1.0 ) )

cmds.xform( 'R_Eye_Piv', t=( 6.485136625973131, 207.31325998101738, 226.21829151157678 ), ro=( 5.939935635096861, 1.8369896653334559, 5.922171239648797 ), s=( 1.0, 1.0, 1.0 ) )


# -------------------------------------------------------
# create eyeball rigs

# L
L_EyeRigRet = denBR.den_makeEyeRig( side='L_', name='Eye', radius=1, ctrlRadius=20.0, displayLocalAxis=False )
print( L_EyeRigRet )
L_EyeRigGrp = L_EyeRigRet[0]; print( L_EyeRigGrp )
L_EyeSpaceINs = L_EyeRigRet[1]; print( L_EyeSpaceINs )
L_EyeSpaceOUTs = L_EyeRigRet[2]; print( L_EyeSpaceOUTs )
L_EyeBindJnts = L_EyeRigRet[3]; print( L_EyeBindJnts )
L_EyeCtrlsALL = L_EyeRigRet[4]; print( L_EyeCtrlsALL )
L_EyeGutsALL = L_EyeRigRet[5]; print( L_EyeGutsALL )

L_EyeHeadSpaceIN = L_EyeSpaceINs[0]
L_EyeRigGrp = cmds.parent( L_EyeRigGrp, RootRigGrp )

# R
R_EyeRigRet = denBR.den_makeEyeRig( side='R_', name='Eye', radius=1, ctrlRadius=20.0, displayLocalAxis=False )
print( R_EyeRigRet )
R_EyeRigGrp = R_EyeRigRet[0]; print( R_EyeRigGrp )
R_EyeSpaceINs = R_EyeRigRet[1]; print( R_EyeSpaceINs )
R_EyeSpaceOUTs = R_EyeRigRet[2]; print( R_EyeSpaceOUTs )
R_EyeBindJnts = R_EyeRigRet[3]; print( R_EyeBindJnts )
R_EyeCtrlsALL = R_EyeRigRet[4]; print( R_EyeCtrlsALL )
R_EyeGutsALL = R_EyeRigRet[5]; print( R_EyeGutsALL )

R_EyeHeadSpaceIN = R_EyeSpaceINs[0]
R_EyeRigGrp = cmds.parent( R_EyeRigGrp, RootRigGrp )

# clean up
denUt.den_connectProxyGeo( Jnts=L_EyeBindJnts+R_EyeBindJnts )

cmds.parentConstraint( HeadSpaceOUT, L_EyeHeadSpaceIN, mo=True )
cmds.parentConstraint( HeadSpaceOUT, R_EyeHeadSpaceIN, mo=True )

denUt.den_AddSafetyCovers( rigGroup=L_EyeRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', L_EyeRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', L_EyeRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', L_EyeRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Left_Color', L_EyeRigGrp[0]+'.Ctrl_Color' )

denUt.den_AddSafetyCovers( rigGroup=R_EyeRigGrp[0] )

# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', R_EyeRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', R_EyeRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', R_EyeRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Right_Color', R_EyeRigGrp[0]+'.Ctrl_Color' )


######################
######## ============================= WHISKER =========================================
# ---------------------------------------------------------------------------------------
# make whisker using Sluggy tail pivots

WhiskerPivRet = denSR.den_makeTailPivs( prefix='L_', name='Whisker', jointCount=8, radius=1 )
# capture all pivots in a variable
WhiskerPivGrp = WhiskerPivRet
# parent pivots under root pivot group
cmds.parent( WhiskerPivGrp, RootPivGrp )


cmds.xform( 'L_Whisker01_Piv', t=( 3.7940426227946817, 204.5701924483856, 239.5730556888628 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_Whisker02_Piv', t=( 9.488205971788558, 204.5701924483856, 239.55465592434342 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_Whisker03_Piv', t=( 15.826084072302145, 204.5701924483856, 239.57043003642528 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_Whisker04_Piv', t=( 22.140609558228242, 204.5701924483856, 239.57141847854453 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_Whisker05_Piv', t=( 28.49071219833399, 204.5701924483856, 239.5878049510801 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_Whisker06_Piv', t=( 34.80348175936142, 204.5701924483856, 239.57794573074622 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_Whisker07_Piv', t=( 41.1530485750239, 204.5701924483856, 239.57888230004193 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_Whisker08_Piv', t=( 47.465655571882586, 204.5701924483856, 239.56493619063363 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_WhiskerEnd_Piv', t=( 53.833936042219115, 204.5701924483856, 239.59446480963325 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )


WhiskerPivRet = denSR.den_makeTailPivs( prefix='R_', name='Whisker', jointCount=8, radius=1 )
# capture all pivots in a variable
WhiskerPivGrp = WhiskerPivRet
# parent pivots under root pivot group
cmds.parent( WhiskerPivGrp, RootPivGrp )

# position tail pivots

cmds.xform( 'R_Whisker01_Piv', t=( -3.7940426227946817, 204.5701924483856, 239.5730556888628 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_Whisker02_Piv', t=( -9.488205971788558, 204.5701924483856, 239.55465592434342 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_Whisker03_Piv', t=( -15.826084072302145, 204.5701924483856, 239.57043003642528 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_Whisker04_Piv', t=( -22.140609558228242, 204.5701924483856, 239.57141847854453 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_Whisker05_Piv', t=( -28.49071219833399, 204.5701924483856, 239.5878049510801 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_Whisker06_Piv', t=( -34.80348175936142, 204.5701924483856, 239.57794573074622 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_Whisker07_Piv', t=( -41.1530485750239, 204.5701924483856, 239.57888230004193 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_Whisker08_Piv', t=( -47.465655571882586, 204.5701924483856, 239.56493619063363 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_WhiskerEnd_Piv', t=( -53.833936042219115, 204.5701924483856, 239.59446480963325 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )

# LLLLLLLLLLLLL ---------------------------------------------------------------------------------------
# make whisker using  Sluggy tail rig (for full IK/FK blendable tail)

L_WhiskerRigRet = denSR.den_makeTailRig( prefix='L_', name='Whisker', jointCount=8, radius=1, ctrlRadius=1.0, controlJoints=(1,4,8), dpTime=0.01  )
print( L_WhiskerRigRet )


# capture the rig group in a variable
L_WhiskerRigGrp = L_WhiskerRigRet[0]; print( L_WhiskerRigGrp )
# capture spaceIn, spaceOUT, BindJoints, Controls, and Guts in 5 variables
L_WhiskerSpaceINs = L_WhiskerRigRet[1]; print( L_WhiskerSpaceINs )
L_WhiskerSpaceOUTs = L_WhiskerRigRet[2]; print( L_WhiskerSpaceOUTs )
L_WhiskerBindJnts = L_WhiskerRigRet[3]; print( L_WhiskerBindJnts )
L_WhiskerCtrlsALL = L_WhiskerRigRet[4]; print( L_WhiskerCtrlsALL )
L_WhiskerGutsALL = L_WhiskerRigRet[5]; print( L_WhiskerGutsALL )
L_WhiskerHandles = L_WhiskerRigRet[6]; print( L_WhiskerHandles )
# make new variables for later connecting attributes
L_WhiskerSpaceIN = L_WhiskerSpaceINs[0]; print( L_WhiskerSpaceIN )


# connect to geometry
denUt.den_connectProxyGeo( Jnts=L_WhiskerBindJnts )

# parent rig under root rig group
L_WhiskerRigGrp = cmds.parent( L_WhiskerRigGrp, RootRigGrp )

# Connect translate/rotate/scale of spaceINs to its spaceOUTs with constraint
cmds.parentConstraint( HeadSpaceOUT, L_WhiskerSpaceIN, mo=True )
cmds.scaleConstraint( HeadSpaceOUT, L_WhiskerSpaceIN, mo=True )


# -----------------------------------------
# make Sluggy tail rig dynamics (only works for IK or IK/FK-blendable tails, does not support FK tails)

L_WhiskerDynRet = denSR.den_addTailDynamics( prefix='L_', name='Whisker', TailRigGrp=L_WhiskerRigGrp, TailSpaceIN=L_WhiskerSpaceIN, TailHandles=L_WhiskerHandles, TailBindJnts=L_WhiskerBindJnts, dpTime=0.01 )
print( L_WhiskerDynRet )

# capture the rig dynamics group in a variable
L_WhiskerDynCtrl = L_WhiskerDynRet[0]; print( L_WhiskerDynCtrl )

# den - customize dynamics attributes here if necessary
cmds.setAttr( L_WhiskerDynCtrl+'.stretchResistance', 100 )
cmds.setAttr( L_WhiskerDynCtrl+'.compressionResistance', 100 )
cmds.setAttr( L_WhiskerDynCtrl+'.bendResistance', 20 )
cmds.setAttr( L_WhiskerDynCtrl+'.startCurveAttract', 0.01 )

# add safetycovers and etc.
denUt.den_AddSafetyCovers( rigGroup=L_WhiskerRigGrp[0] )

# connect controls visibility attribute to the AllCtrl
cmds.connectAttr( AllCtrl+'.Show_Controls', L_WhiskerRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', L_WhiskerRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', L_WhiskerRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Left_Color', L_WhiskerRigGrp[0]+'.Ctrl_Color' )



# RRRRRRRRRRRRR ---------------------------------------------------------------------------------------
# make whisker using  Sluggy tail rig (for full IK/FK blendable tail)

R_WhiskerRigRet = denSR.den_makeTailRig( prefix='R_', name='Whisker', jointCount=8, radius=1, ctrlRadius=1.0, controlJoints=(1,4,8), dpTime=0.01  )
print( R_WhiskerRigRet )

# capture the rig group in a variable
R_WhiskerRigGrp = R_WhiskerRigRet[0]; print( R_WhiskerRigGrp )
# capture spaceIn, spaceOUT, BindJoints, Controls, and Guts in 5 variables
R_WhiskerSpaceINs = R_WhiskerRigRet[1]; print( R_WhiskerSpaceINs )
R_WhiskerSpaceOUTs = R_WhiskerRigRet[2]; print( R_WhiskerSpaceOUTs )
R_WhiskerBindJnts = R_WhiskerRigRet[3]; print( R_WhiskerBindJnts )
R_WhiskerCtrlsALL = R_WhiskerRigRet[4]; print( R_WhiskerCtrlsALL )
R_WhiskerGutsALL = R_WhiskerRigRet[5]; print( R_WhiskerGutsALL )
R_WhiskerHandles = R_WhiskerRigRet[6]; print( R_WhiskerHandles )
# make new variables for later connecting attributes
R_WhiskerSpaceIN = R_WhiskerSpaceINs[0]; print( R_WhiskerSpaceIN )


# connect to geometry
denUt.den_connectProxyGeo( Jnts=R_WhiskerBindJnts )

# parent rig under root rig group
R_WhiskerRigGrp = cmds.parent( R_WhiskerRigGrp, RootRigGrp )

# Connect translate/rotate/scale of spaceINs to its spaceOUTs with constraint
cmds.parentConstraint( HeadSpaceOUT, R_WhiskerSpaceIN, mo=True )
cmds.scaleConstraint( HeadSpaceOUT, R_WhiskerSpaceIN, mo=True )

#######
# -----------------------------------------
# make Sluggy tail rig dynamics (only works for IK or IK/FK-blendable tails, does not support FK tails)

R_WhiskerDynRet = denSR.den_addTailDynamics( prefix='R_', name='Whisker', TailRigGrp=R_WhiskerRigGrp, TailSpaceIN=R_WhiskerSpaceIN, TailHandles=R_WhiskerHandles, TailBindJnts=R_WhiskerBindJnts, dpTime=0.01 )
print( R_WhiskerDynRet )

# capture the rig dynamics group in a variable
R_WhiskerDynCtrl = R_WhiskerDynRet[0]; print( R_WhiskerDynCtrl )

# den - customize dynamics attributes here if necessary
cmds.setAttr( R_WhiskerDynCtrl+'.stretchResistance', 100 )
cmds.setAttr( R_WhiskerDynCtrl+'.compressionResistance', 100 )
cmds.setAttr( R_WhiskerDynCtrl+'.bendResistance', 20 )
cmds.setAttr( R_WhiskerDynCtrl+'.startCurveAttract', 0.01 )

# add safetycovers and etc.
denUt.den_AddSafetyCovers( rigGroup=R_WhiskerRigGrp[0] )

# connect controls visibility attribute to the AllCtrl
cmds.connectAttr( AllCtrl+'.Show_Controls', R_WhiskerRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', R_WhiskerRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', R_WhiskerRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Right_Color', R_WhiskerRigGrp[0]+'.Ctrl_Color' )


######## ============================= TONGUE =========================================
# ---------------------------------------------------------------------------------------
# make Sluggy tail pivots
TonguePivRet = denSR.den_makeTailPivs( prefix='', name='Tongue', jointCount=8, radius=1 )
# capture all pivots in a variable
TonguePivGrp = TonguePivRet
# parent pivots under root pivot group
cmds.parent( TonguePivGrp, RootPivGrp )

# position tail pivots
cmds.xform( 'Tongue01_Piv', t=( 0.0, 192.26641677024722, 221.58356827195422 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'Tongue02_Piv', t=( 0.0, 192.8057524676036, 225.30424001995908 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'Tongue03_Piv', t=( 0.0, 193.07542031628182, 229.22683237538777 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'Tongue04_Piv', t=( 0.0, 193.04171183519705, 233.97319271192725 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'Tongue05_Piv', t=( 0.0, 192.8057524676036, 239.4512307520541 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'Tongue06_Piv', t=( 0.0, 192.5360846189254, 244.2424038829195 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'Tongue07_Piv', t=( 0.0, 192.26641677024716, 249.46394753511947 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'Tongue08_Piv', t=( 0.0, 192.26641677024716, 253.9600622421747 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'TongueEnd_Piv', t=( 0.0, 192.26641677024716, 258.1290010186599 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )


# ---------------------------------------------------------------------------------------
# make Sluggy tail rig (for full IK/FK blendable tail)

TongueRigRet = denSR.den_makeTailRig( prefix='', name='Tongue', jointCount=8, radius=1, ctrlRadius=2.0, controlJoints=(1,4,8), dpTime=0.01  )
print( TongueRigRet )

# capture the rig group in a variable
TongueRigGrp = TongueRigRet[0]; print( TongueRigGrp )
# capture spaceIn, spaceOUT, BindJoints, Controls, and Guts in 5 variables
TongueSpaceINs = TongueRigRet[1]; print( TongueSpaceINs )
TongueSpaceOUTs = TongueRigRet[2]; print( TongueSpaceOUTs )
TongueBindJnts = TongueRigRet[3]; print( TongueBindJnts )
TongueCtrlsALL = TongueRigRet[4]; print( TongueCtrlsALL )
TongueGutsALL = TongueRigRet[5]; print( TongueGutsALL )
TongueHandles = TongueRigRet[6]; print( TongueHandles )
# make new variables for later connecting attributes
TongueSpaceIN = TongueSpaceINs[0]; print( TongueSpaceIN )


# connect to geometry
denUt.den_connectProxyGeo( Jnts=TongueBindJnts )

# parent rig under root rig group
TongueRigGrp = cmds.parent( TongueRigGrp, RootRigGrp )

# Connect translate/rotate/scale of spaceINs to its spaceOUTs with constraint
cmds.parentConstraint( HeadSpaceOUT, TongueSpaceIN, mo=True )
cmds.scaleConstraint( HeadSpaceOUT, TongueSpaceIN, mo=True )


# ---------------------------------------------------------------------------------------
# make Sluggy tail rig dynamics (only works for IK or IK/FK-blendable tails, does not support FK tails)

TongueDynRet = denSR.den_addTailDynamics( prefix='', name='Tongue', TailRigGrp=TongueRigGrp, TailSpaceIN=TongueSpaceIN, TailHandles=TongueHandles, TailBindJnts=TongueBindJnts, dpTime=0.01 )
print( TongueDynRet )

# capture the rig dynamics group in a variable
TongueDynCtrl = TongueDynRet[0]; print( TongueDynCtrl )

# den - customize dynamics attributes here if necessary
cmds.setAttr( TongueDynCtrl+'.stretchResistance', 100 )
cmds.setAttr( TongueDynCtrl+'.compressionResistance', 100 )
cmds.setAttr( TongueDynCtrl+'.bendResistance', 20 )
cmds.setAttr( TongueDynCtrl+'.startCurveAttract', 0.01 )

# add safetycovers and etc.
denUt.den_AddSafetyCovers( rigGroup=TongueRigGrp[0] )

# connect controls visibility attribute to the AllCtrl
cmds.connectAttr( AllCtrl+'.Show_Controls', TongueRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', TongueRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', TongueRigGrp[0]+'.Bone_Draw_Style' )
cmds.connectAttr( AllCtrl+'.Center_Color', TongueRigGrp[0]+'.Ctrl_Color' )

# ---------------------------------------------------------------------------------------
#########################
# ===================================================================================================
# half muscle helpers
# ===================================================================================================

# make thigh helper pivots
# Edit: for thigh, i reverse pivot postion and the aim from twist02 to twist03
L_ThighHelpPiv = denBR.den_makeHalfMusclePivs( side='L_', prefix='', name='ThighHelp', radius=2.0, dpTime=0.01 )
L_ThighHelpPiv = cmds.parent( L_ThighHelpPiv, RootPivGrp )
R_ThighHelpPiv = denBR.den_makeHalfMusclePivs( side='R_', prefix='', name='ThighHelp', radius=2.0, dpTime=0.01 )
R_ThighHelpPiv = cmds.parent( R_ThighHelpPiv, RootPivGrp )

# reposition pivots
cmds.xform( 'L_ThighHelpRoot_Piv', t=( 13.176769784629737, 109.50627136230469, -40.96072006225586 ), ro=( 119.23003655290935, 57.87926463276772, -43.63135403290764 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_ThighHelpRootUp_Piv', t=( 26.52844452600093, 75.37274925522466, -41.79780292942931 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'L_ThighHelpTip_Piv', t=( 25.13425636291504, 98.10682678222656, -67.27558507456769 ), ro=( 119.23003655290935, 57.87926463276772, -43.63135403290763 ), s=( 1.0, 1.0, 1.0 ) )

cmds.xform( 'R_ThighHelpRoot_Piv', t=( 13.176769784629737, 109.50627136230469, -40.96072006225586 ), ro=( 119.23003655290935, 57.87926463276772, -43.63135403290764 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_ThighHelpRootUp_Piv', t=( 26.52844452600093, 75.37274925522466, -41.79780292942931 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'R_ThighHelpTip_Piv', t=( 25.13425636291504, 98.10682678222656, -67.27558507456769 ), ro=( 119.23003655290935, 57.87926463276772, -43.63135403290763 ), s=( 1.0, 1.0, 1.0 ) )


# - add SpaceOUTs to the joints that will have either the root or tip of the halfMuscles connected to them
L_HipTwist03_Jnt_SpaceOUT = denUt.den_AddSpaceOUTs(Jnts=['L_HipTwist03_Jnt'])
R_HipTwist03_Jnt_SpaceOUT = denUt.den_AddSpaceOUTs(Jnts=['R_HipTwist03_Jnt'])
Spine02_Jnt_SpaceOUT = denUt.den_AddSpaceOUTs(Jnts=['Spine02_Jnt'])

Chest_SpaceOUT = TorsoSpaceOUTs[4]
Neck01_SpaceOUT = TorsoSpaceOUTs[5]
Neck02_SpaceOUT = TorsoSpaceOUTs[6]
Neck03_SpaceOUT = TorsoSpaceOUTs[7]
Jaw_SpaceOUT = TorsoSpaceOUTs[12]


# make L thigh helper
L_ThighHelpRigRet = denBR.den_makeHalfMuscleRig( side='L_', prefix='', name='ThighHelp', radius=3.0 )
print( L_ThighHelpRigRet )
L_ThighHelpRigGrp = L_ThighHelpRigRet[0]; print( L_ThighHelpRigGrp )
L_ThighHelpSpaceINs = L_ThighHelpRigRet[1]; print( L_ThighHelpSpaceINs )
L_ThighHelpSpaceOUTs = L_ThighHelpRigRet[2]; print( L_ThighHelpSpaceOUTs )
L_ThighHelpBindJoints = L_ThighHelpRigRet[3]; print( L_ThighHelpBindJoints )
L_ThighHelpCtrlsALL = L_ThighHelpRigRet[4]; print( L_ThighHelpCtrlsALL )
L_ThighHelpGutsALL = L_ThighHelpRigRet[5]; print( L_ThighHelpGutsALL )
#
L_ThighHelpRootSpaceIN = L_ThighHelpSpaceINs[0]
L_ThighHelpTipSpaceIN = L_ThighHelpSpaceINs[1]
#
L_ThighHelpRigGrp = cmds.parent( L_ThighHelpRigGrp, RootRigGrp )
#
# since i edited thigh helper's aim, this need to be switched too
cmds.parentConstraint( Spine02_Jnt_SpaceOUT, L_ThighHelpRootSpaceIN, mo=True )
cmds.parentConstraint( L_HipTwist03_Jnt_SpaceOUT, L_ThighHelpTipSpaceIN, mo=True )
#
cmds.scaleConstraint( Spine02_Jnt_SpaceOUT, L_ThighHelpRootSpaceIN, mo=True )
cmds.scaleConstraint( L_HipTwist03_Jnt_SpaceOUT, L_ThighHelpTipSpaceIN, mo=True )
#
print (L_ThighHelpRigGrp)
# connect Controls visibility to the All_Ctrl
denUt.den_AddSafetyCovers( rigGroup=L_ThighHelpRigGrp[0] )
#
# connect stretchable display proxy to proxy visibility on all control
cmds.connectAttr( AllCtrl+'.Show_Proxy_Geo', 'L_ThighHelp_DispMesh.visibility', force=True, lock=True )
#
# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', L_ThighHelpRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', L_ThighHelpRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', L_ThighHelpRigGrp[0]+'.Bone_Draw_Style' )

# make R thigh helper
R_ThighHelpRigRet = denBR.den_makeHalfMuscleRig( side='R_', prefix='', name='ThighHelp', radius=2.0 )
print( R_ThighHelpRigRet )
R_ThighHelpRigGrp = R_ThighHelpRigRet[0]; print( R_ThighHelpRigGrp )
R_ThighHelpSpaceINs = R_ThighHelpRigRet[1]; print( R_ThighHelpSpaceINs )
R_ThighHelpSpaceOUTs = R_ThighHelpRigRet[2]; print( R_ThighHelpSpaceOUTs )
R_ThighHelpBindJoints = R_ThighHelpRigRet[3]; print( R_ThighHelpBindJoints )
R_ThighHelpCtrlsALL = R_ThighHelpRigRet[4]; print( R_ThighHelpCtrlsALL )
R_ThighHelpGutsALL = R_ThighHelpRigRet[5]; print( R_ThighHelpGutsALL )
#
R_ThighHelpRootSpaceIN = R_ThighHelpSpaceINs[0]
R_ThighHelpTipSpaceIN = R_ThighHelpSpaceINs[1]
#
R_ThighHelpRigGrp = cmds.parent( R_ThighHelpRigGrp, RootRigGrp )
#
# since i edited thigh helper's aim, this need to be switched too
cmds.parentConstraint( Spine02_Jnt_SpaceOUT, R_ThighHelpRootSpaceIN, mo=True )
cmds.parentConstraint( R_HipTwist03_Jnt_SpaceOUT, R_ThighHelpTipSpaceIN, mo=True )
#
cmds.scaleConstraint( Spine02_Jnt_SpaceOUT, R_ThighHelpRootSpaceIN, mo=True )
cmds.scaleConstraint( R_HipTwist03_Jnt_SpaceOUT, R_ThighHelpTipSpaceIN, mo=True )
#
# connect Controls visibility to the All_Ctrl
denUt.den_AddSafetyCovers( rigGroup=R_ThighHelpRigGrp[0] )
#
# connect stretchable display proxy to proxy visibility on all control
cmds.connectAttr( AllCtrl+'.Show_Proxy_Geo', 'R_ThighHelp_DispMesh.visibility', force=True, lock=True )
#
# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', R_ThighHelpRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', R_ThighHelpRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', R_ThighHelpRigGrp[0]+'.Bone_Draw_Style' )

# ----------------------------
### Make THROAT


ThroatPiv = denBR.den_makeHalfMusclePivs( side='', prefix='', name='Throat', radius=2.0, dpTime=0.01 )
ThroatPiv = cmds.parent( ThroatPiv, RootPivGrp )

cmds.xform( 'ThroatRoot_Piv', t=( 0.0, 185.77804792784747, 200.16559271039264 ), ro=( -90.00000000000014, -79.26270106593329, -89.99999999999987 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'ThroatRootUp_Piv', t=( 0.0, 174.97481310951375, 210.07838457543647 ), ro=( 0.0, 0.0, 0.0 ), s=( 1.0, 1.0, 1.0 ) )
cmds.xform( 'ThroatTip_Piv', t=( 0.0, 182.33348670684632, 218.33059227533076 ), ro=( -90.00000000000014, -79.26270106593329, -89.99999999999997 ), s=( 1.0, 1.0, 1.0 ) )


ThroatRigRet = denBR.den_makeHalfMuscleRig( side='', prefix='', name='Throat', radius=2.0 )
print( ThroatRigRet )
ThroatRigGrp = ThroatRigRet[0]; print( ThroatRigGrp )
ThroatSpaceINs = ThroatRigRet[1]; print( ThroatSpaceINs )
ThroatSpaceOUTs = ThroatRigRet[2]; print( ThroatSpaceOUTs )
ThroatBindJoints = ThroatRigRet[3]; print( ThroatBindJoints )
ThroatCtrlsALL = ThroatRigRet[4]; print( ThroatCtrlsALL )
ThroatGutsALL = ThroatRigRet[5]; print( ThroatGutsALL )
#
ThroatRootSpaceIN = ThroatSpaceINs[0]
ThroatTipSpaceIN = ThroatSpaceINs[1]
#
ThroatRigGrp = cmds.parent( ThroatRigGrp, RootRigGrp )
#
cmds.parentConstraint( Neck03_SpaceOUT, ThroatRootSpaceIN, mo=True )
cmds.parentConstraint( Jaw_SpaceOUT, ThroatTipSpaceIN, mo=True )
#
cmds.scaleConstraint( Neck03_SpaceOUT, ThroatRootSpaceIN, mo=True )
cmds.scaleConstraint( Jaw_SpaceOUT, ThroatTipSpaceIN, mo=True )
#
# connect Controls visibility to the All_Ctrl
denUt.den_AddSafetyCovers( rigGroup=ThroatRigGrp[0] )
#
# connect stretchable display proxy to proxy visibility on all control
cmds.connectAttr( AllCtrl+'.Show_Proxy_Geo', 'Throat_DispMesh.visibility', force=True, lock=True )
#
# connect Controls visibility to the All_Ctrl
cmds.connectAttr( AllCtrl+'.Show_Controls', ThroatRigGrp[0]+'.Show_Controls' )
cmds.connectAttr( AllCtrl+'.Show_Guts', ThroatRigGrp[0]+'.Show_Guts' )
cmds.connectAttr( AllCtrl+'.Bone_Draw_Style', ThroatRigGrp[0]+'.Bone_Draw_Style' )



'''
#################################


# ---------------------------------------------------------------------------------------


# ===================================================================================================
# ---------------------------- Paint Weight Transfer ----------------------------
# Use this section of code after you've completed the proxy model rig.
# This script transfers skin weights from the proxy model to your final render geometry,
# giving you a solid starting point for further weight painting and refinement.
# ===================================================================================================


# -------------------------------------------------------------------------------------------
# set up the body point weighting

BindJoints = cmds.ls( '*_Jnt' )
Meshes = [s.replace('_Jnt', '_Mesh') for s in BindJoints] # only includes joints with matching proxy meshes

for number, node in enumerate(BindJoints):
    mesh = cmds.ls( Meshes[number] )
    print(number, BindJoints[number], mesh)

print(BindJoints)
print(Meshes)

# temporarily bind the proxy geometry to its matching _Jnt
denUt.den_tempBindProxyGeo( Jnts=BindJoints )

# do the initial capture from the body _Jnt joints
BodySkinClust = cmds.skinCluster( 'Body_Geo', BindJoints, tsb=True, name='Body_Geo_skinCluster' )[0]

# select the proxy meshes, then the body geometry last
cmds.select( Meshes )
cmds.select( 'Body_Geo', add=True )

# transfer weights from proxy meshes to body geometry to make good starting point for weight painting
cmds.copySkinWeights( noMirror=True, surfaceAssociation='closestPoint', influenceAssociation='closestJoint' )

# remove temporary binding of proxy geo to avoid double transforms
for number, node in enumerate(BindJoints):
    print(number, BindJoints[number], Meshes[number])
    cmds.skinCluster( Meshes[number], e=True, ub=True )

######################################################################

######## ============================= apply skin weight for eyes =========================================
# Bind both eyeballs to the render geo rig
EyeBindJoints = cmds.ls( '*_Eye_Jnt' )
print(EyeBindJoints)
# Bind weight for both eyeballs
EyesSkinClust = cmds.skinCluster( 'Eyes_Geo', EyeBindJoints, tsb=True, name='Eyes_Geo_skinCluster', mi=1 )[0]


# -------------------------------------------------------------------------------------------
# Now we have the basic skin weights. You can refine your weight manuly.
# -------------------------------------------------------------------------------------------
#################################
'''
