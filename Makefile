all: addons

design/competitiveness_management.xmi: design/competitiveness_management.zargo
	-echo "REBUILD competitiveness_management.xmi from competitiveness_management.zargo. I cant do it"

addons: competitiveness_management

competitiveness_management: design/competitiveness_management.uml
	xmi2oerp -r -i $< -t addons -v 2

clean:
	mv addons/README ./README_addons_clean
	rm -rf addons/competitiveness_management/*
	mv README_addons_clean addons/README
	sleep 1
	touch design/competitiveness_management.uml
