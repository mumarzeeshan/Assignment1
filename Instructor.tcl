#############################################################################
# Generated by PAGE version 4.9
# in conjunction with Tcl version 8.6
set vTcl(timestamp) ""


set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #d9d9d9
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #d8d8d8
set vTcl(active_menu_fg) #000000
#############################################################################
# vTcl Code to Load User Fonts

vTcl:font:add_font \
    "-family {Segoe UI Black} -size 11 -weight bold -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font10
vTcl:font:add_font \
    "-family {Segoe UI Black} -size 24 -weight bold -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font12
#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top37
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    set site_3_0 $base.fra38
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# USER DEFINED PROCEDURES
#

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top37 {base} {
    if {$base == ""} {
        set base .top37
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background {#333333} 
    wm focusmodel $top passive
    wm geometry $top 729x552+359+93
    update
    # set in toplevel.wgt.
    global vTcl
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1362 741
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "CreateAQuiz"
    vTcl:DefineAlias "$top" "InstructorView" vTcl:Toplevel:WidgetProc "" 1
    frame $top.fra38 \
        -borderwidth 1 -relief groove -background {#00ffff} -height 275 \
        -width 385 
    vTcl:DefineAlias "$top.fra38" "CreationFrame" vTcl:WidgetProc "InstructorView" 1
    set site_3_0 $top.fra38
    label $site_3_0.cpd40 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#333333} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#ffffff} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text Description 
    vTcl:DefineAlias "$site_3_0.cpd40" "DescriptionLabel" vTcl:WidgetProc "InstructorView" 1
    entry $site_3_0.cpd42 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_3_0.cpd42" "DescriptionEntry" vTcl:WidgetProc "InstructorView" 1
    button $site_3_0.but44 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#333333} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#ffffff} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Submit 
    vTcl:DefineAlias "$site_3_0.but44" "LogInButton" vTcl:WidgetProc "InstructorView" 1
    label $site_3_0.cpd46 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#333333} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#ffffff} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Title 
    vTcl:DefineAlias "$site_3_0.cpd46" "TitleLabel" vTcl:WidgetProc "InstructorView" 1
    entry $site_3_0.cpd47 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_3_0.cpd47" "TitleEntry" vTcl:WidgetProc "InstructorView" 1
    place $site_3_0.cpd40 \
        -in $site_3_0 -x 70 -y 90 -width 254 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode inside 
    place $site_3_0.cpd42 \
        -in $site_3_0 -x 71 -y 121 -width 254 -relwidth 0 -height 100 \
        -relheight 0 -anchor nw -bordermode inside 
    place $site_3_0.but44 \
        -in $site_3_0 -x 140 -y 230 -width 107 -relwidth 0 -height 24 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.cpd46 \
        -in $site_3_0 -x 70 -y 30 -width 254 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode inside 
    place $site_3_0.cpd47 \
        -in $site_3_0 -x 70 -y 60 -width 254 -relwidth 0 -height 20 \
        -relheight 0 -anchor nw -bordermode inside 
    label $top.lab45 \
        -background {#333333} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font12,object) -foreground {#ffffff} \
        -text {Create a quiz} 
    vTcl:DefineAlias "$top.lab45" "Logo" vTcl:WidgetProc "InstructorView" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra38 \
        -in $top -x 190 -y 140 -width 385 -relwidth 0 -height 275 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab45 \
        -in $top -x 260 -y 80 -width 211 -relwidth 0 -height 41 -relheight 0 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

#############################################################################
## Binding tag:  _TopLevel

bind "_TopLevel" <<Create>> {
    if {![info exists _topcount]} {set _topcount 0}; incr _topcount
}
bind "_TopLevel" <<DeleteWindow>> {
    if {[set ::%W::_modal]} {
                vTcl:Toplevel:WidgetProc %W endmodal
            } else {
                destroy %W; if {$_topcount == 0} {exit}
            }
}
bind "_TopLevel" <Destroy> {
    if {[winfo toplevel %W] == "%W"} {incr _topcount -1}
}

Window show .
Window show .top37

