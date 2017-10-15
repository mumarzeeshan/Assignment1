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
    vTcl:font9
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
        -background {#333333} -highlightbackground {#d9d9d9} \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 731x552+357+93
    update
    # set in toplevel.wgt.
    global vTcl
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1362 741
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "Quiz"
    vTcl:DefineAlias "$top" "Quiz" vTcl:Toplevel:WidgetProc "" 1
    frame $top.fra38 \
        -borderwidth 1 -relief groove -background {#00ffff} -height 285 \
        -highlightbackground {#d9d9d9} -highlightcolor black -width 525 
    vTcl:DefineAlias "$top.fra38" "CreationFrame" vTcl:WidgetProc "Quiz" 1
    set site_3_0 $top.fra38
    label $site_3_0.lab40 \
        -background {#333333} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#ffffff} \
        -text Q: 
    vTcl:DefineAlias "$site_3_0.lab40" "Question" vTcl:WidgetProc "Quiz" 1
    button $site_3_0.but42 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#333333} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#ffffff} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text {Next Question} 
    vTcl:DefineAlias "$site_3_0.but42" "Next" vTcl:WidgetProc "Quiz" 1
    label $site_3_0.lab43 \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -text a 
    vTcl:DefineAlias "$site_3_0.lab43" "a" vTcl:WidgetProc "Quiz" 1
    label $site_3_0.cpd44 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text b 
    vTcl:DefineAlias "$site_3_0.cpd44" "b" vTcl:WidgetProc "Quiz" 1
    label $site_3_0.cpd45 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text c 
    vTcl:DefineAlias "$site_3_0.cpd45" "c" vTcl:WidgetProc "Quiz" 1
    label $site_3_0.cpd46 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text d 
    vTcl:DefineAlias "$site_3_0.cpd46" "d" vTcl:WidgetProc "Quiz" 1
    entry $site_3_0.ent47 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -insertbackground black 
    vTcl:DefineAlias "$site_3_0.ent47" "UserAnswer" vTcl:WidgetProc "Quiz" 1
    place $site_3_0.lab40 \
        -in $site_3_0 -x 60 -y 30 -width 394 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but42 \
        -in $site_3_0 -x 200 -y 220 -width 107 -relwidth 0 -height 34 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab43 \
        -in $site_3_0 -x 60 -y 70 -width 134 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.cpd44 \
        -in $site_3_0 -x 61 -y 121 -width 134 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode inside 
    place $site_3_0.cpd45 \
        -in $site_3_0 -x 311 -y 71 -width 144 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode inside 
    place $site_3_0.cpd46 \
        -in $site_3_0 -x 310 -y 120 -width 144 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode inside 
    place $site_3_0.ent47 \
        -in $site_3_0 -x 190 -y 180 -width 124 -relwidth 0 -height 20 \
        -relheight 0 -anchor nw -bordermode ignore 
    label $top.lab45 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#333333} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#ffffff} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Quiz 
    vTcl:DefineAlias "$top.lab45" "Logo" vTcl:WidgetProc "Quiz" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra38 \
        -in $top -x 100 -y 140 -width 525 -relwidth 0 -height 285 \
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

