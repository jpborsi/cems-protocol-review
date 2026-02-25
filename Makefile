clean:
	rm -r raw_protocol
	rm -r text_protocol
	rm -r review

protocol.pdf:
	curl https://cecoms.cuyahogacounty.gov/pdf/RegionalEMSProtocol.pdf > protocol.pdf

raw_protocol: protocol.pdf
	mkdir -p raw_protocol
	uv run split.py protocol.pdf 2026R1_protocols.yaml raw_protocol

text_protocol: raw_protocol
	mkdir -p text_protocol
	scripts/extract_all.sh

review/openai: text_protocol
	mkdir -p review/openai
	scripts/review_all.sh

review/openai_combined_review.csv: review/openai
	scripts/combine_csv.sh