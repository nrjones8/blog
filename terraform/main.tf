variable "aws_region" {
  default = "us-west-2"
}

variable "domain_name" {
  default = "nrjones8.me"
}

provider "aws" {
  region = "${var.aws_region}"
}

resource "aws_s3_bucket" "personal_website_bucket" {
  bucket = "${var.domain_name}"
  acl    = "public-read"
  policy = "${file("s3_website_policy.json")}"

  website {
    index_document = "index.html"
    error_document = "error.html"
  }
}

# Just redirect `www` to the above bucket
resource "aws_s3_bucket" "www_personal_website_bucket" {
  bucket = "www.${var.domain_name}"

  website {
    redirect_all_requests_to = "${aws_s3_bucket.personal_website_bucket.id}"
  }
}

# Created this in the console, then imported it. I'm not sure it's worth the trouble of importing
# the nameservers - they're never really going to be changed? A little over my head at this point,
# so let's just let it be
resource "aws_route53_zone" "website_dot_me_zone" {
  # Not entirely sure where the trailing period is necessary...
  name = "${var.domain_name}."
}

# Point domain name at the S3 bucket containing website content
resource "aws_route53_record" "root_domain" {
  zone_id = "${aws_route53_zone.website_dot_me_zone.zone_id}"
  name    = "${var.domain_name}"
  type    = "A"

  # http://blakesmith.me/2016/04/02/terraform-aws-static-site-with-cloudfront.html
  alias {
    name                   = "${aws_s3_bucket.personal_website_bucket.website_domain}"
    zone_id                = "${aws_s3_bucket.personal_website_bucket.hosted_zone_id}"
    evaluate_target_health = false
  }
}

resource "aws_route53_record" "www_domain" {
  zone_id = "${aws_route53_zone.website_dot_me_zone.zone_id}"
  name    = "www.${var.domain_name}"
  type    = "A"

  # http://blakesmith.me/2016/04/02/terraform-aws-static-site-with-cloudfront.html
  alias {
    name                   = "${aws_s3_bucket.personal_website_bucket.website_domain}"
    zone_id                = "${aws_s3_bucket.personal_website_bucket.hosted_zone_id}"
    evaluate_target_health = false
  }
}

terraform {
  # The config used here should probably be created in a separate, account-wide TF module that
  # would be used by any other terraform I might want to use. But for now, the backend S3 bucket
  # and the lock table were created manually :-( :-(
  backend "s3" {
    bucket = "nick-terraform"

    dynamodb_table = "tf_lock"
    key            = "personal-website/terraform.state"
    region         = "us-west-2"
  }

  required_version = "~> 0.10.4"
}
